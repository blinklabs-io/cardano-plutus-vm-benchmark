#!/usr/bin/env python3
"""Generate markdown and HTML comparison reports from unified.csv."""

import csv
import html
import json
import math
import os
import re
import sys
from collections import defaultdict

VM_ORDER = [
    "haskell", "scalus-jit", "scalus-cek",
    "julc-java",
    "llvm-uplc-jit",
    "amaru-uplc", "aiken", "plutus-machine",
    "plutuz", "chrysalis", "chrysalis-aot",
    "plutigo", "blaze-jsc", "blaze-v8", "opshin",
]
VM_LABELS = {
    "amaru-uplc": "Amaru UPLC CEK (Rust)",
    "aiken": "Aiken UPLC CEK (Rust)",
    "plutus-machine": "Harmonic Labs plutus-machine CEK (TypeScript / Node.js)",
    "plutuz": "Plutuz CEK (Zig)",
    "chrysalis": "Chrysalis CEK (C# / .NET)",
    "chrysalis-aot": "Chrysalis CEK (C# / .NET AOT)",
    "plutigo": "Plutigo CEK (Go)",
    "blaze-jsc": "blaze-plutus CEK (TypeScript / Bun JSC)",
    "blaze-v8": "blaze-plutus CEK (TypeScript / Node V8)",
    "opshin": "opshin CEK (Python / CPython)",
    "haskell": "plutus-core CEK (Haskell / GHC)",
    "scalus-cek": "Scalus CEK (Scala / JVM)",
    "scalus-jit": "Scalus UPLC→JVM JIT (Scala / JVM)",
    "julc-java": "Julc CEK (Java / GraalVM)",
    "llvm-uplc-jit": "llvm-uplc post-JIT execution (C++ / LLVM)",
}


def vm_labels(versions: dict) -> dict:
    """VM_LABELS, naming plutus-machine's runtime as the run recorded it.

    plutus-machine ran on Node.js until its adapter moved to Bun, so the
    runtime comes from the run's toolchain; a run that recorded none ran on
    Node.js.
    """
    labels = dict(VM_LABELS)
    toolchain = versions.get("plutus-machine", {}).get("toolchain", "")
    if toolchain.startswith("Bun"):
        labels["plutus-machine"] = labels["plutus-machine"].replace("Node.js", "Bun JSC")
    return labels


def fmt_ns(ns: int) -> str:
    """Format nanoseconds into human-readable string."""
    if ns >= 1_000_000_000:
        return f"{ns / 1e9:.2f} s"
    if ns >= 1_000_000:
        return f"{ns / 1e6:.2f} ms"
    if ns >= 1_000:
        return f"{ns / 1e3:.2f} us"
    return f"{ns} ns"


def geometric_mean(values: list[float]) -> float:
    """Compute geometric mean of positive values."""
    if not values:
        return 0
    log_sum = sum(math.log(v) for v in values if v > 0)
    return math.exp(log_sum / len(values))


# Measurement tiers, in report order. Runs from before tiers were recorded
# have no tier column; their rows are read as the full tier.
TIERS = ["full", "eval"]
TIER_TITLES = {
    "full": "Full tier: decode and evaluate",
    "eval": "Eval tier: evaluate a decoded program",
}
TIER_NOTES = {
    "full": "Each iteration decodes the whole .flat file, including its Data arguments, and evaluates it.",
    "eval": "The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.",
}


# Corpora, in page order. Runs from before corpora were recorded measured
# plutus_use_cases.
CORPORA = ["plutus_use_cases", "mainnet_recent"]
CORPUS_TITLES = {
    "plutus_use_cases": "Plutus use cases",
    "mainnet_recent": "Mainnet validators",
}
CORPUS_NOTES = {
    "plutus_use_cases": "Real-world contracts from the plutus-use-cases test suite (auction, escrow, uniswap, stablecoin and others).",
    "mainnet_recent": "Validators from recent mainnet transactions, each applied to the datum, redeemer and script context it ran with on mainnet.",
}
CORPUS_LINE = re.compile(
    r"^corpus: (?P<corpus>\S+) \((?P<count>\d+) of (?P<total>\d+) programs"
    r"(?: from (?P<tx_count>\d+) of (?P<tx_total>\d+) transactions)?, "
    r"sample (?P<sample>\S+), seed (?P<seed>[^;)]+)",
    re.MULTILINE,
)


def corpus_info(run_dir: str, env_info: str, scripts) -> dict:
    """Return the corpus a run measured: name, sample size, seed and programs."""
    m = CORPUS_LINE.search(env_info)
    corpus_path = os.path.join(run_dir, "corpus.txt")
    if os.path.isfile(corpus_path):
        with open(corpus_path) as f:
            programs = [line.strip().removesuffix(".flat") for line in f if line.strip()]
    else:
        programs = sorted(scripts)
    if m:
        return {
            "corpus": m["corpus"],
            "count": int(m["count"]),
            "total": int(m["total"]),
            "sample": m["sample"],
            "seed": m["seed"],
            "tx_count": int(m["tx_count"]) if m["tx_count"] else None,
            "tx_total": int(m["tx_total"]) if m["tx_total"] else None,
            "programs": programs,
        }
    return {
        "corpus": "plutus_use_cases",
        "count": len(programs),
        "total": len(programs),
        "sample": "all",
        "seed": None,
        "tx_count": None,
        "tx_total": None,
        "programs": programs,
    }


def corpus_programs(corpus: str) -> list[str]:
    """Return the complete set of programs tracked for a corpus."""
    if corpus not in CORPORA:
        return []
    corpus_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", corpus)
    if not os.path.isdir(corpus_dir):
        return []
    return sorted(
        name.removesuffix(".flat")
        for name in os.listdir(corpus_dir)
        if name.endswith(".flat")
    )


def complete_transaction_ids(scripts, complete_scripts) -> set[str]:
    """Return transaction IDs whose complete corpus script groups are present."""
    expected = defaultdict(set)
    for script in complete_scripts:
        match = TRANSACTION_NAME.match(script)
        if match:
            expected[match[1]].add(script)

    present = defaultdict(set)
    for script in scripts:
        match = TRANSACTION_NAME.match(script)
        if match:
            present[match[1]].add(script)

    return {
        tx for tx, tx_scripts in present.items()
        if expected.get(tx) == tx_scripts
    }


def corpus_summary(info: dict) -> str:
    """One line describing a run's corpus, for the report."""
    title = CORPUS_TITLES.get(info["corpus"], info["corpus"])
    if info["tx_count"] and info["tx_count"] < info["tx_total"]:
        return (f"{title} (`{info['corpus']}`): every script of {info['tx_count']} of {info['tx_total']} "
                f"transactions ({info['count']} of {info['total']} programs), selected with seed {info['seed']}")
    if info["count"] < info["total"]:
        return (f"{title} (`{info['corpus']}`): {info['count']} of {info['total']} programs, "
                f"selected with seed {info['seed']}")
    return f"{title} (`{info['corpus']}`): all {info['total']} programs"


def load_data(run_dir: str):
    """Load unified.csv and return (tiers, env_info).

    tiers maps each tier with results to (data, scripts, present_vms), where
    data maps script to VM to mean_ns.
    """
    unified_path = os.path.join(run_dir, "unified.csv")
    if not os.path.isfile(unified_path):
        print("Error: unified.csv not found", file=sys.stderr)
        sys.exit(1)

    by_tier: dict[str, dict[str, dict[str, int]]] = defaultdict(lambda: defaultdict(dict))
    with open(unified_path) as f:
        for row in csv.DictReader(f):
            tier = row.get("tier") or "full"
            by_tier[tier][row["script"]][row["vm"]] = int(row["mean_ns"])

    tiers = {}
    for tier in TIERS:
        if tier not in by_tier:
            continue
        data = by_tier[tier]
        scripts = sorted(data.keys())
        present_vms = [vm for vm in VM_ORDER if any(vm in data[s] for s in scripts)]
        tiers[tier] = (data, scripts, present_vms)

    env_path = os.path.join(run_dir, "environment.txt")
    env_info = ""
    if os.path.isfile(env_path):
        with open(env_path) as f:
            env_info = f.read().strip()

    return tiers, env_info


def load_versions(run_dir: str):
    """Load source revisions and toolchains recorded for a benchmark run."""
    versions_path = os.path.join(run_dir, "versions.csv")
    versions = {}
    if os.path.isfile(versions_path):
        with open(versions_path, newline="") as f:
            for row in csv.DictReader(f):
                versions[row["vm"]] = row
    return versions


# Mainnet programs are named "<transaction id>-<purpose>-<index>".
TRANSACTION_NAME = re.compile(r"^([0-9a-f]{64})-")


def transaction_totals(data, scripts, present_vms, complete_transactions):
    """Sum each VM's times over every script of each transaction.

    Returns None unless every program is named after a transaction. Incomplete
    corpus groups are omitted. A VM that failed any script fails the transaction
    (-1); one missing a script without failing one has no total for it.
    """
    runs = defaultdict(list)
    for script in scripts:
        m = TRANSACTION_NAME.match(script)
        if not m:
            return None
        runs[m[1]].append(script)
    totals = {}
    for tx, tx_scripts in runs.items():
        if tx not in complete_transactions:
            continue
        totals[tx] = {}
        for vm in present_vms:
            times = [data[s].get(vm, 0) for s in tx_scripts]
            if all(t > 0 for t in times):
                totals[tx][vm] = sum(times)
            elif any(t < 0 for t in times):
                totals[tx][vm] = -1
    return totals


def compute_geo_means(data, scripts, present_vms):
    """Compute geometric means with penalty for missing scripts.

    When a VM hasn't implemented a benchmark script, it gets assigned
    the score of the slowest competitor on that script. This prevents
    VMs from gaming the leaderboard by selectively skipping slow tests.
    """
    geo_means: dict[str, float] = {}

    for vm in present_vms:
        values = []
        for s in scripts:
            t = data[s].get(vm, 0)
            if t > 0:
                values.append(t)
            else:
                # Missing or failed: assign the slowest successful time
                # from any other VM on this script
                worst = max(
                    (data[s].get(other_vm, 0) for other_vm in present_vms if other_vm != vm),
                    default=0,
                )
                if worst > 0:
                    values.append(worst)
                # If no VM has a result for this script, skip it entirely

        geo_means[vm] = geometric_mean(values)

    return geo_means


def generate_markdown(run_dir: str, tiers, env_info, versions) -> None:
    """Generate report.md."""
    labels = vm_labels(versions)
    present_vms = [
        vm for vm in VM_ORDER
        if any(vm in tier_vms for _, _, tier_vms in tiers.values())
    ]

    lines = []
    lines.append("# Cardano Plutus VM Benchmark Results")
    lines.append("")
    lines.append(f"**Date:** {run_date(run_dir, env_info)}")
    lines.append("")
    all_scripts = sorted({s for _, scripts, _ in tiers.values() for s in scripts})
    info = corpus_info(run_dir, env_info, all_scripts)
    complete_scripts = corpus_programs(info["corpus"])
    lines.append(f"**Corpus:** {corpus_summary(info)}. The per-script tables list every program measured.")
    lines.append("")

    if env_info:
        lines.append("## Environment")
        lines.append("```")
        lines.append(env_info)
        lines.append("```")
        lines.append("")

    recorded_versions = [vm for vm in present_vms if vm in versions]
    if recorded_versions:
        lines.append("## VM Versions")
        lines.append("")
        lines.append("| VM | Source revision | Toolchain |")
        lines.append("|---|---|---|")
        for vm in recorded_versions:
            version = versions[vm]
            repo = version.get("repo", "unknown")
            version_label = version.get("version", "unknown")
            revision = version.get("revision", "unknown")
            toolchain = version.get("toolchain", "unknown")
            if repo != "unknown" and revision != "unknown":
                source = repo.removesuffix(".git") + f"/commit/{revision}"
                if version_label == "commit" or version_label == "unknown":
                    version_label = "commit"
                revision = f"{version_label} ([{revision[:7]}]({source}))"
            elif repo != "unknown":
                revision = f"[{version_label}]({repo})"
            else:
                revision = version_label
            lines.append(f"| {labels.get(vm, vm)} | {revision} | {toolchain} |")
        lines.append("")

    lines.append("*Measurement caveats: llvm-uplc and Scalus JIT report execution after JIT compilation; llvm-uplc's per-script compilation time is retained only in the raw JSON. Scalus JIT, Scalus CEK, Julc and Chrysalis use three measurement samples, and their raw framework output should be consulted for uncertainty.*")
    lines.append("")

    for tier, (data, scripts, tier_vms) in tiers.items():
        append_tier(lines, tier, data, scripts, tier_vms, complete_scripts, labels)

    lines.append("---")
    lines.append("*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*")

    report = "\n".join(lines)
    report_path = os.path.join(run_dir, "report.md")
    with open(report_path, "w") as f:
        f.write(report)

    print(report)
    print(f"\nReport saved to: {report_path}", file=sys.stderr)


def append_tier(lines, tier, data, scripts, present_vms, complete_scripts, labels) -> None:
    """Append one tier's summary, coverage and per-script tables."""
    geo_means = compute_geo_means(data, scripts, present_vms)
    fastest_geo = min(geo_means.values()) if geo_means else 1

    lines.append(f"## {TIER_TITLES.get(tier, tier)}")
    lines.append("")
    lines.append(TIER_NOTES.get(tier, ""))
    lines.append("")

    complete_transactions = complete_transaction_ids(scripts, complete_scripts)
    totals = transaction_totals(data, scripts, present_vms, complete_transactions)
    if totals:
        transactions = sorted(totals)
        tx_means = compute_geo_means(totals, transactions, present_vms)
        tx_fastest = min(v for v in tx_means.values() if v > 0) if any(v > 0 for v in tx_means.values()) else 1
        lines.append(f"### Per transaction (geometric mean of {len(transactions)} transaction totals)")
        lines.append("")
        lines.append("*Each VM's time for a transaction is the sum of its times for every script the transaction runs. "
                     "A VM that fails any script fails the transaction, which is assigned the slowest competitor's total.*")
        lines.append("")
        lines.append("| VM | Language | Geo Mean | vs Fastest | Failed transactions |")
        lines.append("|---|---|---|---|---|")
        ranked_vms = sorted(present_vms, key=lambda vm: (tx_means[vm] <= 0, tx_means[vm]))
        for vm in ranked_vms:
            label = labels.get(vm, vm)
            lang = label.split("(")[-1].rstrip(")") if "(" in label else ""
            geo = tx_means[vm]
            failed = sum(1 for tx in transactions if totals[tx].get(vm, 0) < 0)
            if geo > 0:
                lines.append(f"| **{label}** | {lang} | {fmt_ns(int(geo))} | {geo / tx_fastest:.2f}x | {failed} |")
            else:
                lines.append(f"| **{label}** | {lang} | n/a | n/a | {failed} |")
        lines.append("")

    lines.append("### Summary (geometric mean across all scripts)")
    lines.append("")
    lines.append("*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*")
    lines.append("")
    lines.append("| VM | Language | Geo Mean | vs Fastest |")
    lines.append("|---|---|---|---|")

    sorted_vms = sorted(present_vms, key=lambda vm: geo_means.get(vm, float("inf")))
    for vm in sorted_vms:
        label = labels.get(vm, vm)
        lang = label.split("(")[-1].rstrip(")") if "(" in label else ""
        geo = geo_means[vm]
        ratio = geo / fastest_geo if fastest_geo > 0 else 0
        lines.append(f"| **{label}** | {lang} | {fmt_ns(int(geo))} | {ratio:.2f}x |")

    # Count scripts per VM
    lines.append("")
    lines.append("#### Script Coverage")
    lines.append("")
    lines.append("| VM | Passed | Failed | Missing | Total |")
    lines.append("|---|---|---|---|---|")
    for vm in sorted_vms:
        success = sum(1 for s in scripts if data[s].get(vm, 0) > 0)
        fail = sum(1 for s in scripts if data[s].get(vm, 0) < 0)
        missing = len(scripts) - success - fail
        lines.append(f"| {labels.get(vm, vm)} | {success} | {fail} | {missing} | {len(scripts)} |")

    lines.append("")

    lines.append("### Per-Script Results")
    lines.append("")
    header = "| Script |" + "|".join(f" {labels.get(vm, vm)} " for vm in present_vms) + "|"
    separator = "|---|" + "|".join("---" for _ in present_vms) + "|"
    lines.append(header)
    lines.append(separator)

    for script in scripts:
        row = f"| {script} |"
        script_times = {vm: data[script].get(vm, 0) for vm in present_vms}
        fastest = min((t for t in script_times.values() if t > 0), default=0)

        for vm in present_vms:
            t = script_times[vm]
            if t > 0:
                cell = fmt_ns(t)
                if t == fastest and len([v for v in script_times.values() if v > 0]) > 1:
                    cell = f"**{cell}**"
                row += f" {cell} |"
            elif t < 0:
                row += " FAIL |"
            else:
                row += " - |"
        lines.append(row)

    lines.append("")


def run_date(run_dir: str, env_info: str) -> str:
    """The day a run started, from environment.txt, else its directory name."""
    m = re.search(r"^date: (\d{4}-\d{2}-\d{2})", env_info, re.MULTILINE)
    return m[1] if m else os.path.basename(run_dir)


def env_badge(run_dir: str, env_info: str) -> str:
    """The environment line shown in the page header."""
    badge = ""
    for line in env_info.split("\n"):
        key, _, value = line.strip().partition(":")
        key = key.strip().lower()
        value = html.escape(value.strip())
        if key == "cpu":
            badge += f"<code>{value}</code>"
        elif key == "cores":
            badge += f" &middot; {value} cores"
        elif key in {"memory", "ram"}:
            badge += f" &middot; {value}"
        elif key in {"kernel", "os"}:
            badge += f" &middot; {value}"
    date = run_date(run_dir, env_info)
    return f"{badge} &middot; {date}" if badge else date


def page_run(run_dir: str) -> dict:
    """One run's data for the page."""
    tiers, env_info = load_data(run_dir)
    with open(os.path.join(run_dir, "unified.csv")) as f:
        csv_data = f.read().strip()
    versions_path = os.path.join(run_dir, "versions.csv")
    if os.path.isfile(versions_path):
        with open(versions_path) as f:
            versions_data = f.read().strip()
    else:
        versions_data = "vm,repo,version,revision,toolchain"
    scripts = sorted({s for _, tier_scripts, _ in tiers.values() for s in tier_scripts})
    info = corpus_info(run_dir, env_info, scripts)
    complete_scripts = corpus_programs(info["corpus"])
    return {
        **info,
        "complete_transactions": {
            tier: sorted(complete_transaction_ids(tier_scripts, complete_scripts))
            for tier, (_, tier_scripts, _) in tiers.items()
        },
        "title": CORPUS_TITLES.get(info["corpus"], info["corpus"]),
        "note": CORPUS_NOTES.get(info["corpus"], ""),
        "date": run_date(run_dir, env_info),
        "env": env_badge(run_dir, env_info),
        "env_text": env_info,
        "csv": csv_data,
        "versions": versions_data,
    }


def generate_html(run_dirs: list[str]) -> None:
    """Generate docs/index.html from the template and one run per corpus."""
    template_path = os.path.join(os.path.dirname(__file__), "template.html")
    if not os.path.isfile(template_path):
        print("Warning: report/template.html not found, skipping HTML generation", file=sys.stderr)
        return
    with open(template_path) as f:
        template = f.read()

    newest: dict[str, dict] = {}
    for run in (page_run(run_dir) for run_dir in run_dirs):
        held = newest.get(run["corpus"])
        if held is None or run["date"] >= held["date"]:
            newest[run["corpus"]] = run
    runs = list(newest.values())
    order = {corpus: i for i, corpus in enumerate(CORPORA)}
    runs.sort(key=lambda r: order.get(r["corpus"], len(CORPORA)))
    # Any "<" could open "</script>" or "<!--<script>", which changes how the
    # parser ends the inline script.
    runs_json = json.dumps(runs).replace("<", "\\u003c")
    html = template.replace("{{RUNS_JSON}}", runs_json)

    # Write to docs/index.html (relative to repo root)
    repo_root = os.path.dirname(os.path.dirname(__file__))
    docs_dir = os.path.join(repo_root, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    html_path = os.path.join(docs_dir, "index.html")
    with open(html_path, "w") as f:
        f.write(html)

    print(f"HTML report saved to: {html_path}", file=sys.stderr)


def natural_key(name: str):
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", name)]


def latest_runs(results_dir: str) -> list[str]:
    """The newest run of each corpus under results_dir."""
    latest: dict[str, str] = {}
    for name in sorted(os.listdir(results_dir), key=natural_key):
        run_dir = os.path.join(results_dir, name)
        if not os.path.isfile(os.path.join(run_dir, "unified.csv")):
            continue
        env_path = os.path.join(run_dir, "environment.txt")
        env_info = open(env_path).read() if os.path.isfile(env_path) else ""
        m = CORPUS_LINE.search(env_info)
        latest[m["corpus"] if m else "plutus_use_cases"] = run_dir
    return list(latest.values())


def generate(run_dirs: list[str]) -> None:
    for run_dir in run_dirs:
        tiers, env_info = load_data(run_dir)
        versions = load_versions(run_dir)
        generate_markdown(run_dir, tiers, env_info, versions)
    generate_html(run_dirs)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "--latest":
        run_dirs = latest_runs(args[1])
        if not run_dirs:
            sys.exit(f"no runs with unified.csv in {args[1]}")
    elif args and not args[0].startswith("-"):
        run_dirs = args
    else:
        print(f"Usage: {sys.argv[0]} <run-dir>... | --latest <results-dir>", file=sys.stderr)
        sys.exit(1)
    generate(run_dirs)
