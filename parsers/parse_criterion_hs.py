#!/usr/bin/env python3
"""Parse Haskell Criterion CSV benchmark output into unified CSV.

Criterion's --csv flag produces:
  Name,Mean,MeanLB,MeanUB,Stddev,StddevLB,StddevUB
where Mean/Stddev are in seconds.
"""

import csv
import sys
from collections import OrderedDict

VM_NAME = "haskell"
HEADER = "vm,script,mean_ns,median_ns,min_ns,max_ns,stddev_ns,iterations"


def parse(csv_path: str) -> None:
    # Use OrderedDict to deduplicate — last occurrence wins (handles aborted reruns)
    results: OrderedDict[str, str] = OrderedDict()

    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Name"]
            # Skip duplicate header rows
            if name == "Name":
                continue
            # Extract script name: "validation/script-name" → "script-name"
            script = name.split("/")[-1] if "/" in name else name

            mean_s = float(row["Mean"])
            stddev_s = float(row["Stddev"])
            mean_ns = int(mean_s * 1e9)
            stddev_ns = int(stddev_s * 1e9)

            results[script] = (
                f"{VM_NAME},{script},"
                f"{mean_ns},-1,-1,-1,"
                f"{stddev_ns},-1"
            )

    print(HEADER)
    for line in results.values():
        print(line)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <criterion-csv-file>", file=sys.stderr)
        sys.exit(1)
    parse(sys.argv[1])
