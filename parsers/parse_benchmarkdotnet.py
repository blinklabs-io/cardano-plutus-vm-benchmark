#!/usr/bin/env python3
"""Parse BenchmarkDotNet JSON benchmark output into unified CSV."""

import json
import os
import re
import sys

VM_NAME = "chrysalis"  # default; overridden by CLI arg
HEADER = "vm,script,mean_ns,median_ns,min_ns,max_ns,stddev_ns,iterations"

# Benchmark method for each tier: DecodeAndEval decodes in the timed method,
# Eval (added by harness/chrysalis/eval-tier.patch) evaluates the program
# decoded in [GlobalSetup].
TIER_METHODS = {"full": "DecodeAndEval", "eval": "Eval"}

# BenchmarkDotNet reports times with unit suffixes
UNIT_MULTIPLIERS = {
    "ns": 1,
    "us": 1_000,
    "\u03bcs": 1_000,  # mu-s unicode
    "ms": 1_000_000,
    "s": 1_000_000_000,
}


def parse_time_ns(value) -> int:
    """Convert a BDN time value to nanoseconds."""
    if isinstance(value, (int, float)):
        return int(value)
    # String with unit suffix
    s = str(value).strip()
    for unit, mult in UNIT_MULTIPLIERS.items():
        if s.endswith(unit):
            return int(float(s[: -len(unit)].strip()) * mult)
    return int(float(s))


# BenchmarkDotNet shortens a long parameter value for display, keeping its
# start and end and appending its length: "8e4034e230b1771(...)02d5b00-spend-0 [72]".
SHORTENED = re.compile(r"^(?P<head>.*)\(\.\.\.\)(?P<tail>.*) \[(?P<length>\d+)\]$")


def full_script_name(name: str, data_dir: str | None) -> str:
    """Map a shortened parameter value back to its .flat file in data_dir."""
    m = SHORTENED.match(name)
    if not m or not data_dir:
        return name
    head, tail, length = m["head"], m["tail"], int(m["length"])
    matches = [
        n[: -len(".flat")]
        for n in os.listdir(data_dir)
        if n.endswith(".flat")
    ]
    matches = [
        n for n in matches
        if len(n) == length and n.startswith(head) and n.endswith(tail)
    ]
    if len(matches) != 1:
        sys.exit(f"cannot map shortened script name {name!r}: {len(matches)} matches in {data_dir}")
    return matches[0]


def parse(run_dir: str, tier: str = "full") -> None:
    data_dir = os.environ.get("BENCH_DATA_DIR")
    method = TIER_METHODS[tier]
    print(HEADER)

    # Find BDN JSON report files
    json_files = []
    for root, _, files in os.walk(run_dir):
        for f in files:
            if f.endswith(".json") and "PlutusUseCases" in f:
                json_files.append(os.path.join(root, f))

    if not json_files:
        # Try the standard BDN output path
        artifacts_dir = os.path.join(run_dir)
        for root, _, files in os.walk(artifacts_dir):
            for f in files:
                if f.endswith("-report.json"):
                    json_files.append(os.path.join(root, f))

    for json_file in json_files:
        with open(json_file) as f:
            data = json.load(f)

        benchmarks = data.get("Benchmarks", [])
        for bench in benchmarks:
            if bench.get("Method", "DecodeAndEval") != method:
                continue
            # Extract script name from parameters
            params = bench.get("Parameters", "")
            script_name = params.replace("Script=", "") if params else bench.get(
                "MethodTitle", "unknown"
            )
            script_name = full_script_name(script_name, data_dir)

            stats = bench.get("Statistics", {})
            mean_ns = parse_time_ns(stats.get("Mean", 0))
            median_ns = parse_time_ns(stats.get("Median", 0))
            min_ns = parse_time_ns(stats.get("Min", 0))
            max_ns = parse_time_ns(stats.get("Max", 0))
            stddev_ns = parse_time_ns(stats.get("StandardDeviation", 0))
            iterations = stats.get("N", 0)

            print(
                f"{VM_NAME},{script_name},"
                f"{mean_ns},{median_ns},{min_ns},{max_ns},"
                f"{stddev_ns},{iterations}"
            )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [vm-name] <run-dir> [tier]", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) >= 3:
        VM_NAME = sys.argv[1]
        parse(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "full")
    else:
        parse(sys.argv[1])
