"""Tests for the public FizzBuzz API and command-line entry point."""

import subprocess
import sys
import unittest
from pathlib import Path

from fizzbuzz import fizzbuzz


SCRIPT = Path(__file__).with_name("fizzbuzz.py")


class FizzBuzzTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True, text=True, check=False,
        )

    def test_api(self):
        self.assertEqual(fizzbuzz(0), [])
        self.assertEqual(fizzbuzz(15)[-3:], ["13", "14", "FizzBuzz"])

    def test_default_count(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.splitlines(), fizzbuzz(15))

    def test_custom_count(self):
        result = self.run_cli("30")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.splitlines(), fizzbuzz(30))

    def test_invalid_count(self):
        for args in (("0",), ("-2",), ("abc",), ("2.5",), ("15", "30")):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("error:", result.stderr)


if __name__ == "__main__":
    unittest.main()
