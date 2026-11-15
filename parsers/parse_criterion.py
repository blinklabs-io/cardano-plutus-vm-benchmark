#!/usr/bin/env python3
"""Parse Criterion.rs JSON benchmark output into unified CSV."""

import json
import os
import sys

HEADER = "vm,script,mean_ns,median_ns,min_ns,max_ns,stddev_ns,iterations"


def parse(criterion_dir: str, vm_name: str = "amaru-uplc") -> None:
    print(HEADER)

    if not os.path.isdir(criterion_dir):
        print(f"Warning: {criterion_dir} not found", file=sys.stderr)
        return

    # Criterion shortens a benchmark's directory name to 64 characters, so the
    # script name comes from new/benchmark.json. Each script may have its own
    # CRITERION_HOME below criterion_dir, so search the whole tree.
    bench_dirs = sorted(
        os.path.dirname(root)
        for root, _, files in os.walk(criterion_dir)
        if os.path.basename(root) == "new" and "estimates.json" in files
    )
    for bench_dir in bench_dirs:
        bench_name = os.path.relpath(bench_dir, criterion_dir)
        estimates_path = os.path.join(bench_dir, "new", "estimates.json")

        with open(estimates_path) as f:
            est = json.load(f)

        mean_ns = int(est["mean"]["point_estimate"])
        median_ns = int(est["median"]["point_estimate"])
        stddev_ns = int(est["std_dev"]["point_estimate"])

        # Extract min/max from sample data if available
        sample_path = os.path.join(bench_dir, "new", "sample.json")
        min_ns = 0
        max_ns = 0
        iterations = 0

        if os.path.isfile(sample_path):
            with open(sample_path) as f:
                sample = json.load(f)
            iters = sample.get("iters", [])
            times = sample.get("times", [])
            if iters and times:
                per_iter = [t / i for i, t in zip(iters, times) if i > 0]
                if per_iter:
                    min_ns = int(min(per_iter))
                    max_ns = int(max(per_iter))
                iterations = len(per_iter)

        script_name = os.path.basename(bench_name)
        benchmark_path = os.path.join(bench_dir, "new", "benchmark.json")
        if os.path.isfile(benchmark_path):
            with open(benchmark_path) as f:
                bench = json.load(f)
            script_name = (bench.get("function_id") or bench.get("full_id") or script_name).split("/")[-1]

        print(
            f"{vm_name},{script_name},"
            f"{mean_ns},{median_ns},{min_ns},{max_ns},"
            f"{stddev_ns},{iterations}"
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <criterion-output-dir> [vm-name]", file=sys.stderr)
        sys.exit(1)
    vm = sys.argv[2] if len(sys.argv) > 2 else "amaru-uplc"
    parse(sys.argv[1], vm)
