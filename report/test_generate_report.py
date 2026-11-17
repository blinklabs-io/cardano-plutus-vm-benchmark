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


if __name__ == "__main__":
    unittest.main()
