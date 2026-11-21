import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class PeerUpdateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        script = Path(__file__).with_name("update-pins.sh").read_text()
        cls.program = script.split("node <<'JS'\n", 1)[1].split("\nJS\n", 1)[0]

    def run_update(self, peer_response, version_response=None, failed=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = {"dependencies": {"@harmoniclabs/uplc": "2.0.7", "other": "1.0.0"}}
            manifest = root / "package.json"
            manifest.write_text(json.dumps(package))
            npm = root / "npm"
            npm.write_text("""#!/usr/bin/env python3
import json, os, sys
if os.environ['NPM_VIEW_FAIL'] == '1':
    sys.exit(17)
responses = json.loads(os.environ['NPM_VIEW_RESPONSES'])
sys.stdout.write(responses[sys.argv[2] + ' ' + sys.argv[3]])
""")
            npm.chmod(0o755)
            responses = {"@harmoniclabs/plutus-machine@3.1.0 peerDependencies": peer_response}
            if version_response is not None:
                responses["@harmoniclabs/uplc@^2.0.8 version"] = version_response
            result = subprocess.run(
                ["node"], input=self.program, text=True, capture_output=True,
                cwd=root, env={**os.environ, "PM": "3.1.0", "PATH": str(root) + os.pathsep + os.environ["PATH"],
                               "NPM_VIEW_RESPONSES": json.dumps(responses), "NPM_VIEW_FAIL": str(int(failed))},
            )
            return result, json.loads(manifest.read_text()), package

    def test_missing_peer_dependencies(self):
        for response in ("", " \n\t", "null", "{}"):
            with self.subTest(response=response):
                result, actual, original = self.run_update(response)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(actual, original)

    def test_highest_semantic_version(self):
        cases = [
            (["2.0.8", "2.1.0", "2.0.9"], "2.1.0"),
            (["2.0.10", "2.0.9"], "2.0.10"),
            (["2.10.0", "2.9.99"], "2.10.0"),
            (["10.0.0", "9.99.99"], "10.0.0"),
            (["2.1.0", "2.1.0-rc.10"], "2.1.0"),
            (["2.1.0-rc.10", "2.1.0-rc.2"], "2.1.0-rc.10"),
            (["2.1.0-alpha.beta", "2.1.0-alpha.1"], "2.1.0-alpha.beta"),
            (["2.1.0-alpha.1", "2.1.0-alpha"], "2.1.0-alpha.1"),
            (["2.1.0-a-b", "2.1.0-a-a"], "2.1.0-a-b"),
            (["2.1.0+build.9", "2.1.0+build.1"], "2.1.0+build.9"),
            (["2.0.8"], "2.0.8"),
            ("2.0.8", "2.0.8"),
        ]
        for versions, expected in cases:
            with self.subTest(versions=versions):
                result, actual, _ = self.run_update(
                    json.dumps({"@harmoniclabs/uplc": "^2.0.8", "unused": "*"}), json.dumps(versions)
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(actual["dependencies"]["@harmoniclabs/uplc"], expected)
                self.assertEqual(actual["dependencies"]["other"], "1.0.0")
                self.assertNotIn("unused", actual["dependencies"])

    def test_lookup_failures_remain_fatal(self):
        for peer_response, versions, failed, message in [
            ("{}", None, True, "Command failed: npm view"),
            ("not JSON", None, False, "SyntaxError"),
            ('{"@harmoniclabs/uplc":"^2.0.8"}', "[]", False,
             "no @harmoniclabs/uplc version matches ^2.0.8"),
        ]:
            with self.subTest(peer_response=peer_response, versions=versions, failed=failed):
                result, actual, original = self.run_update(peer_response, versions, failed)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)
                self.assertEqual(actual, original)


if __name__ == "__main__":
    unittest.main()
