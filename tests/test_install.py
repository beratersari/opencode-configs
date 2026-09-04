from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import install  # noqa: E402


class PathHelpers(unittest.TestCase):
    def test_detects_default_and_dedicated_bin(self) -> None:
        self.assertTrue(install.is_opencode_bin_entry(r"C:\Users\x\.opencode\bin"))
        self.assertTrue(install.is_opencode_bin_entry("/home/x/.opencode/bin"))
        self.assertTrue(install.is_opencode_bin_entry(r"C:\tools\opencode\bin"))
        self.assertTrue(install.is_opencode_bin_entry("/opt/opencode/bin"))
        self.assertFalse(install.is_opencode_bin_entry("/usr/local/bin"))
        self.assertFalse(install.is_opencode_bin_entry(r"C:\tools\bin"))
        self.assertFalse(install.is_opencode_bin_entry(""))

    def test_dedicated_root_from_binary(self) -> None:
        import tempfile

        tmp = Path(tempfile.mkdtemp(prefix="ocfg-"))
        self.addCleanup(lambda: __import__("shutil").rmtree(tmp, ignore_errors=True))
        binary = tmp / "apps" / "opencode" / "bin" / "opencode.exe"
        binary.parent.mkdir(parents=True)
        binary.write_text("x", encoding="utf-8")
        root = install.dedicated_install_root(binary)
        self.assertEqual(root, binary.parent.parent)

    def test_strip_removes_only_opencode_bin(self) -> None:
        parts = [r"C:\Windows", r"C:\Users\x\.opencode\bin", r"C:\git\cmd"]
        kept = install.strip_opencode_bin_entries(parts)
        self.assertEqual(kept, [r"C:\Windows", r"C:\git\cmd"])

    def test_profile_block_roundtrip(self) -> None:
        raw = "export PATH=/usr/bin\n"
        written = install.insert_profile_block(raw)
        self.assertIn(install.PATH_BEGIN, written)
        self.assertIn(install.PATH_EXPORT, written)
        cleaned = install.strip_profile_block(written)
        self.assertEqual(cleaned.strip(), "export PATH=/usr/bin")


class ReplaceInstall(unittest.TestCase):
    def test_lists_shipped_agents_and_skills(self) -> None:
        agents = [p.stem for p in install.list_agent_files(ROOT)]
        skills = [p.name for p in install.list_skill_dirs(ROOT)]
        self.assertIn("review", agents)
        self.assertIn("cpp98", skills)
        self.assertIn("modern-cpp", skills)

    def test_purge_removes_homes_and_path(self) -> None:
        import tempfile

        tmp = Path(tempfile.mkdtemp(prefix="ocfg-"))
        self.addCleanup(lambda: __import__("shutil").rmtree(tmp, ignore_errors=True))
        oc = tmp / ".opencode"
        cfg = tmp / ".config" / "opencode"
        (oc / "bin").mkdir(parents=True)
        (oc / "bin" / "old.exe").write_text("old", encoding="utf-8")
        (cfg / "agents").mkdir(parents=True)
        (cfg / "agents" / "stale.md").write_text("stale", encoding="utf-8")
        (tmp / ".opencode-path").write_text(
            install.join_path([str(oc / "bin"), str(tmp / "keep-me")]),
            encoding="utf-8",
        )
        profile = tmp / ".profile"
        profile.write_text(install.insert_profile_block("keep=1\n"), encoding="utf-8")

        dropped = install.remove_from_path(user_home=tmp)
        self.assertTrue(any(install.is_opencode_bin_entry(p) for p in dropped))
        kept = install.split_path((tmp / ".opencode-path").read_text(encoding="utf-8"))
        self.assertEqual(kept, [str(tmp / "keep-me")])
        self.assertNotIn(install.PATH_BEGIN, profile.read_text(encoding="utf-8"))

        install.purge_homes(tmp)
        self.assertFalse(oc.exists())
        self.assertFalse(cfg.exists())

    def test_install_replaces_old_tree(self) -> None:
        import tempfile
        import shutil

        tmp = Path(tempfile.mkdtemp(prefix="ocfg-"))
        self.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))
        old = tmp / ".opencode" / "keep-old.txt"
        old.parent.mkdir(parents=True)
        old.write_text("old", encoding="utf-8")
        (tmp / ".opencode" / "bin").mkdir()
        (tmp / ".opencode-path").write_text(str(tmp / ".opencode" / "bin"), encoding="utf-8")

        dest = install.install(ROOT, user_home=tmp)
        self.assertTrue(dest.is_file())
        self.assertFalse(old.exists())
        self.assertIn("mode: primary", dest.read_text(encoding="utf-8"))
        self.assertTrue((tmp / ".opencode" / "skills" / "cpp98" / "SKILL.md").is_file())
        self.assertTrue((tmp / ".config" / "opencode" / "opencode.json").is_file())
        path = install.split_path((tmp / ".opencode-path").read_text(encoding="utf-8"))
        self.assertTrue(path)
        self.assertTrue(install.is_opencode_bin_entry(path[0]))
        self.assertEqual(len([p for p in path if install.is_opencode_bin_entry(p)]), 1)

    def test_install_picks_up_new_agent_file(self) -> None:
        import tempfile
        import shutil

        tmp = Path(tempfile.mkdtemp(prefix="ocfg-"))
        pack = tmp / "pack"
        shutil.copytree(ROOT / "agents", pack / "agents")
        shutil.copytree(ROOT / "skills", pack / "skills")
        (pack / "agents" / "extra.md").write_text("---\nmode: primary\n---\nextra\n", encoding="utf-8")
        home = tmp / "home"
        install.install(pack, user_home=home)
        self.assertTrue((home / ".config" / "opencode" / "agents" / "extra.md").is_file())

    def test_custom_location_kept_on_disk_removed_from_path(self) -> None:
        import tempfile
        import shutil

        tmp = Path(tempfile.mkdtemp(prefix="ocfg-"))
        self.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))
        home = tmp / "home"
        custom = tmp / "apps" / "opencode" / "bin"
        custom.mkdir(parents=True)
        (custom / "opencode.exe").write_text("old", encoding="utf-8")
        keep = tmp / "keep-me"
        home.mkdir(parents=True)
        (home / ".opencode-path").write_text(
            install.join_path([str(custom), str(keep)]),
            encoding="utf-8",
        )
        install.install(ROOT, user_home=home)
        self.assertTrue((custom / "opencode.exe").is_file())
        path = install.split_path((home / ".opencode-path").read_text(encoding="utf-8"))
        self.assertNotIn(str(custom), path)
        self.assertIn(str(keep), path)
        self.assertTrue((home / ".config" / "opencode" / "agents" / "review.md").is_file())

    def test_shared_bin_files_kept_path_unhooked(self) -> None:
        import tempfile
        import shutil

        tmp = Path(tempfile.mkdtemp(prefix="ocfg-"))
        self.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))
        tools = tmp / "tools" / "bin"
        tools.mkdir(parents=True)
        (tools / "opencode.exe").write_text("old", encoding="utf-8")
        (tools / "git.exe").write_text("git", encoding="utf-8")
        home = tmp / "home"
        (home / ".opencode-path").parent.mkdir(parents=True)
        (home / ".opencode-path").write_text(str(tools), encoding="utf-8")
        install.install(ROOT, user_home=home)
        self.assertTrue((tools / "opencode.exe").is_file())
        self.assertTrue((tools / "git.exe").exists())
        path = install.split_path((home / ".opencode-path").read_text(encoding="utf-8"))
        self.assertNotIn(str(tools), path)


if __name__ == "__main__":
    unittest.main()
