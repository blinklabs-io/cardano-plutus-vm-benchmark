"""Select a reproducible sample of a corpus's .flat programs.

Usage: select_corpus.py CORPUS_DIR OUT_DIR SIZE SEED

Programs are sampled in groups. A program named after a mainnet transaction,
"<64-hex transaction id>-<purpose>-<index>.flat", belongs to that
transaction's group, so a sample keeps every script a transaction runs, as
the ledger validates them together. Any other program is a group of its own.

Every group is ranked by SHA-256 of "<seed>:<group>" and the first SIZE
groups are copied to OUT_DIR, so the same seed always selects the same
programs, on any machine, whatever the directory listing order. SIZE "all"
(or a SIZE at least the number of groups) copies every program.

Prints the selected file names on stdout, and on stderr one line:
"programs=<selected> of <total> groups=<selected> of <total> grouped=<yes|no>".
"""

import hashlib
import os
import re
import shutil
import sys

TRANSACTION = re.compile(r"^([0-9a-f]{64})-")


def group_of(name: str) -> str:
    m = TRANSACTION.match(name)
    return m[1] if m else name


def main() -> None:
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    corpus_dir, out_dir, size, seed = sys.argv[1:]
    names = sorted(n for n in os.listdir(corpus_dir) if n.endswith(".flat"))
    groups = sorted({group_of(n) for n in names})
    chosen = set(groups)
    if size != "all":
        if not size.isdigit() or int(size) < 1:
            sys.exit(f"sample size must be a positive integer or 'all', got {size!r}")
        ranked = sorted(groups, key=lambda g: hashlib.sha256(f"{seed}:{g}".encode()).hexdigest())
        chosen = set(ranked[: int(size)])
    selected = [n for n in names if group_of(n) in chosen]
    os.makedirs(out_dir, exist_ok=True)
    for name in selected:
        shutil.copyfile(os.path.join(corpus_dir, name), os.path.join(out_dir, name))
        print(name)
    grouped = any(TRANSACTION.match(n) for n in names)
    print(
        f"programs={len(selected)} of {len(names)} groups={len(chosen)} of {len(groups)} "
        f"grouped={'yes' if grouped else 'no'}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
