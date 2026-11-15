"""Select a reproducible sample of a corpus's .flat programs.

Usage: select_corpus.py CORPUS_DIR OUT_DIR SIZE SEED

Every program is ranked by SHA-256 of "<seed>:<file name>" and the first SIZE
are copied to OUT_DIR, so the same seed always selects the same programs, on
any machine, whatever the directory listing order. SIZE "all" (or a SIZE at
least the corpus size) copies every program. Prints the selected names.
"""

import hashlib
import os
import shutil
import sys


def main() -> None:
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    corpus_dir, out_dir, size, seed = sys.argv[1:]
    names = sorted(n for n in os.listdir(corpus_dir) if n.endswith(".flat"))
    if size != "all":
        if not size.isdigit() or int(size) < 1:
            sys.exit(f"sample size must be a positive integer or 'all', got {size!r}")
        ranked = sorted(names, key=lambda n: hashlib.sha256(f"{seed}:{n}".encode()).hexdigest())
        names = sorted(ranked[: int(size)])
    os.makedirs(out_dir, exist_ok=True)
    for name in names:
        shutil.copyfile(os.path.join(corpus_dir, name), os.path.join(out_dir, name))
        print(name)


if __name__ == "__main__":
    main()
