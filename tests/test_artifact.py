from __future__ import annotations

import importlib.util
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_builder():
    path = ROOT / "packaging" / "build_artifact.py"
    spec = importlib.util.spec_from_file_location("ocfg_build_artifact", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Artifact(unittest.TestCase):
    def test_zip_contains_agents_and_installers(self) -> None:
        import tempfile

        dest = Path(tempfile.mkdtemp(prefix="ocfg-art-")) / "pack.zip"
        _load_builder().build(ROOT, dest)
        with zipfile.ZipFile(dest) as zf:
            names = set(zf.namelist())
        self.assertIn("agents/review.md", names)
        self.assertIn("skills/cpp98/SKILL.md", names)
        self.assertIn("install.py", names)
        self.assertIn("install.bat", names)
        self.assertIn("install.sh", names)
        self.assertIn("packaging/versions.env", names)

    def test_artifact_name_includes_opencode_version(self) -> None:
        mod = _load_builder()
        version = mod.read_opencode_version(ROOT)
        self.assertEqual(version, "1.18.10")
        self.assertEqual(
            mod.artifact_name(version, "linux"),
            "opencode-configs-1.18.10-linux.zip",
        )
        self.assertEqual(
            mod.artifact_name(version, "windows"),
            "opencode-configs-1.18.10-windows.zip",
        )


if __name__ == "__main__":
    unittest.main()
