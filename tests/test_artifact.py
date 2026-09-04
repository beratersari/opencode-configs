from __future__ import annotations

import importlib.util
import tempfile
import unittest
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
    def test_stage_contains_agents_and_installers(self) -> None:
        dest = Path(tempfile.mkdtemp(prefix="ocfg-art-")) / "pack"
        _load_builder().stage(ROOT, dest)
        self.assertTrue((dest / "agents" / "review.md").is_file())
        self.assertTrue((dest / "skills" / "cpp98" / "SKILL.md").is_file())
        self.assertTrue((dest / "install.py").is_file())
        self.assertTrue((dest / "install.bat").is_file())
        self.assertTrue((dest / "install.sh").is_file())
        self.assertTrue((dest / "packaging" / "versions.env").is_file())
        self.assertFalse(dest.suffix == ".zip")
        self.assertFalse(any(dest.rglob("*.zip")))

    def test_artifact_name_includes_opencode_version(self) -> None:
        mod = _load_builder()
        version = mod.read_opencode_version(ROOT)
        self.assertEqual(version, "1.18.10")
        self.assertEqual(
            mod.artifact_name(version, "linux"),
            "opencode-configs-1.18.10-linux",
        )
        self.assertEqual(
            mod.artifact_name(version, "windows"),
            "opencode-configs-1.18.10-windows",
        )
        self.assertFalse(mod.artifact_name(version, "linux").endswith(".zip"))

    def test_ci_uploads_folder_not_zip(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("upload-artifact", workflow)
        self.assertIn("build_artifact.py", workflow)
        self.assertNotIn(".zip", workflow)
        self.assertNotIn("opencode-configs-*-linux.zip", workflow)
        self.assertNotIn("opencode-configs-*-windows.zip", workflow)


if __name__ == "__main__":
    unittest.main()
