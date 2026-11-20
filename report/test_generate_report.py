import csv
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from report import generate_report


class TransactionRankingTest(unittest.TestCase):
    def test_partial_transaction_is_excluded(self):
        complete_tx = "a" * 64
        partial_tx = "b" * 64
        complete_scripts = [
            f"{complete_tx}-spend-0",
            f"{complete_tx}-withdraw-0",
            f"{partial_tx}-spend-0",
            f"{partial_tx}-withdraw-0",
        ]
        measured_scripts = [
            f"{complete_tx}-spend-0",
            f"{complete_tx}-withdraw-0",
            f"{partial_tx}-spend-0",
        ]

        complete = generate_report.complete_transaction_ids(
            measured_scripts, complete_scripts
        )
        totals = generate_report.transaction_totals(
            {script: {"haskell": 10} for script in measured_scripts},
            measured_scripts,
            ["haskell"],
            complete,
        )

        self.assertEqual(complete, {complete_tx})
        self.assertEqual(totals, {complete_tx: {"haskell": 20}})

    def test_unavailable_transaction_means_are_not_ranked_as_zero(self):
        tx = "c" * 64
        script = f"{tx}-spend-0"
        lines = []

        generate_report.append_tier(
            lines,
            "full",
            {script: {"haskell": 0, "scalus-cek": 0}},
            [script],
            ["haskell", "scalus-cek"],
            [script],
        )

        transaction_table = lines[lines.index("|---|---|---|---|---|") + 1:]
        transaction_rows = transaction_table[:2]
        self.assertEqual(len(transaction_rows), 2)
        self.assertTrue(all("| n/a | n/a |" in row for row in transaction_rows))



class AikenRunnerTest(unittest.TestCase):
    def run_tiers(self, mode):
        with tempfile.TemporaryDirectory() as directory:
            bench = Path(directory)
            root = Path(__file__).resolve().parents[1]
            (bench / "aiken/bin").mkdir(parents=True)
            data = bench / "data/plutus_use_cases"
            data.mkdir(parents=True)
            results = bench / "results"
            results.mkdir()
            parsers = bench / "parsers"
            parsers.mkdir()
            for parser in ("parse_criterion.py", "fill_failures.py"):
                shutil.copy2(root / "parsers" / parser, parsers / parser)
            shutil.copy2(root / "scripts/run-aiken.sh", bench / "run-aiken.sh")
            for name in ("alpha", "beta"):
                (data / (name + ".flat")).write_bytes(b"fixture")
            header = "vm,script,mean_ns,median_ns,min_ns,max_ns,stddev_ns,iterations\n"
            for suffix in ("", "-eval"):
                (results / ("aiken" + suffix + ".csv")).write_text(
                    header + "aiken,alpha,999,999,999,999,0,1\n"
                )
            binary = bench / "aiken/bin/aiken-bench"
            binary.write_text("""#!/usr/bin/env python3
import json, os
from pathlib import Path
name = next(Path(os.environ['PVB_DATA_DIR']).glob('*.flat')).stem
tier = os.environ['PVB_TIER']
with open('/bench/results/calls', 'a') as calls:
    calls.write(tier + ':' + name + '\\n')
if os.environ['MODE'] == 'all' or (os.environ['MODE'] == 'eval' and tier == 'eval' and name == 'alpha'):
    output = Path(os.environ['CRITERION_HOME']) / name / 'new'
    output.mkdir(parents=True)
    estimates = {key: {'point_estimate': value} for key, value in [('mean', 17), ('median', 16), ('std_dev', 2)]}
    (output / 'estimates.json').write_text(json.dumps(estimates))
    (output / 'benchmark.json').write_text(json.dumps({'function_id': name}))
else:
    print('EVAL_FAIL: ' + name)
    raise SystemExit(1)
""")
            binary.chmod(0o755)
            run = subprocess.run([
                "docker", "run", "--rm", "--network", "none",
                "--user", f"{os.getuid()}:{os.getgid()}", "-e", f"MODE={mode}",
                "-v", f"{bench}:/bench", "python:3.14-slim-bookworm",
                "bash", "/bench/run-aiken.sh", "/bench/results",
            ], capture_output=True, text=True)
            self.assertTrue((results / "calls").exists(), run.stderr)
            rows = {}
            for suffix in ("", "-eval"):
                with (results / ("aiken" + suffix + ".csv")).open() as stream:
                    rows[suffix] = {row['script']: int(row['mean_ns']) for row in csv.DictReader(stream)}
            return run.returncode, rows, (results / "calls").read_text()

    def test_empty_tiers_replace_previous_results(self):
        status, rows, calls = self.run_tiers("none")
        self.assertNotEqual(status, 0)
        for suffix in ("", "-eval"):
            self.assertEqual(rows[suffix], {"alpha": -1, "beta": -1})
        self.assertIn("eval:alpha", calls)
        self.assertIn("eval:beta", calls)

    def test_empty_full_tier_keeps_eval_measurements(self):
        status, rows, calls = self.run_tiers("eval")
        self.assertNotEqual(status, 0)
        self.assertEqual(rows[""], {"alpha": -1, "beta": -1})
        self.assertEqual(rows["-eval"], {"alpha": 17, "beta": -1})
        self.assertIn("eval:beta", calls)

    def test_successful_tiers_keep_measurements(self):
        status, rows, _ = self.run_tiers("all")
        self.assertEqual(status, 0)
        self.assertEqual(rows, {"": {"alpha": 17, "beta": 17}, "-eval": {"alpha": 17, "beta": 17}})


if __name__ == "__main__":
    unittest.main()
