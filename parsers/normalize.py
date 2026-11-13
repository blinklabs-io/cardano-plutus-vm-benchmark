#!/usr/bin/env python3
"""Merge per-VM CSV files into a single unified.csv.

Each VM writes up to two files, one per measurement tier:

- ``<vm>.csv``: the full tier, which times decoding the whole .flat file and
  evaluating it in each iteration.
- ``<vm>-eval.csv``: the eval tier, which decodes the program before timing
  and times its evaluation only.

unified.csv records each row's tier in its ``tier`` column.
"""

import csv
import os
import sys

VMS = [
    "chrysalis",
    "chrysalis-aot",
    "amaru-uplc",
    "plutus-machine",
    "plutigo",
    "blaze-jsc",
    "blaze-v8",
    "plutuz",
    "opshin",
    "haskell",
    "scalus-cek",
    "scalus-jit",
    "julc-java",
    "llvm-uplc-jit",
]

TIER_SUFFIXES = {"full": "", "eval": "-eval"}

HEADER = ["vm", "script", "mean_ns", "median_ns", "min_ns", "max_ns", "stddev_ns", "iterations", "tier"]


def normalize(run_dir: str) -> None:
    output_path = os.path.join(run_dir, "unified.csv")
    rows = []

    for vm in VMS:
        for tier, suffix in TIER_SUFFIXES.items():
            vm_file = f"{vm}{suffix}.csv"
            path = os.path.join(run_dir, vm_file)
            if not os.path.isfile(path):
                print(f"  skip: {vm_file} (not found)", file=sys.stderr)
                continue

            with open(path) as f:
                reader = csv.DictReader(f)
                count = 0
                for row in reader:
                    row["tier"] = tier
                    rows.append(row)
                    count += 1
                print(f"  loaded: {vm_file} ({tier} tier, {count} scripts)", file=sys.stderr)

    # Sort by tier, then script name, then VM name
    rows.sort(key=lambda r: (r.get("tier", ""), r.get("script", ""), r.get("vm", "")))

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"  wrote: {output_path} ({len(rows)} total rows)", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <run-dir>", file=sys.stderr)
        sys.exit(1)
    normalize(sys.argv[1])
