from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_project import validate_project  # noqa: E402


class VerifyProjectTests(unittest.TestCase):
    def test_current_project_is_consistent(self) -> None:
        self.assertEqual(validate_project(ROOT), [])


if __name__ == "__main__":
    unittest.main()
