#!/usr/bin/env python3
"""Parse JMH CSV benchmark output into unified CSV.

JMH CSV format (via -rff flag):
  "Benchmark","Mode","Threads","Samples","Score","Score Error (99.9%)","Unit","Param: file"

Score is in the unit specified (typically us/op).
"""

import csv
import sys

HEADER = "vm,script,mean_ns,median_ns,min_ns,max_ns,stddev_ns,iterations"

# Map JMH benchmark method to (VM name, tier). The full tier decodes the
# .flat file inside the timed method; the eval tier decodes it in @Setup.
BENCH_TO_VM = {
    "CekJVMBenchmark.bench": ("scalus-cek", "full"),
    "CekJVMBenchmark.benchEval": ("scalus-cek", "eval"),
    "JITBenchmark.benchJIT": ("scalus-jit", "eval"),
    "CekJavaBenchmark.bench": ("julc-java", "eval"),
}

# Unit conversion to nanoseconds
UNIT_TO_NS = {
    "us/op": 1_000,
    "ms/op": 1_000_000,
    "s/op": 1_000_000_000,
    "ns/op": 1,
}


def parse(csv_path: str, vm_filter: str | None = None, tier: str = "full") -> None:
    print(HEADER)

    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            benchmark = row["Benchmark"]
            # Extract short benchmark name
            short = benchmark.split(".")[-2] + "." + benchmark.split(".")[-1]

            mapped = BENCH_TO_VM.get(short)
            if mapped is None:
                continue
            vm_name, bench_tier = mapped
            if vm_filter and vm_name != vm_filter:
                continue
            if bench_tier != tier:
                continue

            file_param = row.get("Param: file", "")
            script = file_param.replace(".flat", "")
            if not script:
                continue

            score = float(row["Score"])
            unit = row["Unit"]
            samples = int(row["Samples"])

            multiplier = UNIT_TO_NS.get(unit, 1)
            mean_ns = int(score * multiplier)
            # Score Error is a confidence interval, not a standard deviation.
            # JMH's CSV output does not include median, min, max, or stddev.
            median_ns = min_ns = max_ns = stddev_ns = -1

            print(
                f"{vm_name},{script},"
                f"{mean_ns},{median_ns},{min_ns},{max_ns},"
                f"{stddev_ns},{samples}"
            )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <jmh-csv> [vm-filter] [tier]", file=sys.stderr)
        sys.exit(1)
    vm_filter = sys.argv[2] if len(sys.argv) > 2 else None
    tier = sys.argv[3] if len(sys.argv) > 3 else "full"
    parse(sys.argv[1], vm_filter, tier)
