import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import lint_claude_md as lint  # noqa: E402

CLEAN = """# My project

A small service.

## Commands

- Run all tests: `pytest -q`
- Build: `python -m build`

## Style

- Use type hints.
"""


def codes(text):
    return [code for _, code, _ in lint.lint_text(text)]


class LintTests(unittest.TestCase):
    def test_clean_fixture_passes(self):
        self.assertEqual(lint.lint_text(CLEAN), [])

    def test_empty_file(self):
        self.assertEqual(codes(""), ["empty"])
        self.assertEqual(codes("  \n\n"), ["empty"])

    def test_missing_file(self):
        findings = lint.lint_file(os.path.join(ROOT, "does-not-exist.md"))
        self.assertEqual([c for _, c, _ in findings], ["missing"])

    def test_no_top_level_heading(self):
        text = CLEAN.replace("# My project", "Intro line", 1)
        self.assertIn("no-title", codes(text))

    def test_empty_section(self):
        text = CLEAN + "\n## Gotchas\n"
        self.assertIn("empty-section", codes(text))

    def test_placeholders(self):
        for marker in ("TO" + "DO: fix", "<placeholder>", "your-command-here"):
            text = CLEAN + "\n- Note: %s\n" % marker
            self.assertIn("placeholder", codes(text), marker)

    def test_no_commands_section(self):
        text = "# Project\n\n## Style\n\n- Use tabs.\n"
        self.assertIn("no-commands", codes(text))

    def test_long_line(self):
        text = CLEAN + "\n" + "x" * 201 + "\n"
        self.assertIn("long-line", codes(text))
        self.assertNotIn("long-line", codes(CLEAN + "\n" + "x" * 200 + "\n"))

    def test_long_file(self):
        text = CLEAN + "\n- item\n" * 300
        self.assertIn("long-file", codes(text))

    def test_headings_in_code_fence_are_ignored(self):
        text = CLEAN + "\n```\n# not a heading\n```\n"
        self.assertEqual(lint.lint_text(text), [])

    def test_templates_only_have_placeholder_findings(self):
        for name in ("python-library.md", "node-api.md"):
            path = os.path.join(ROOT, "templates", name)
            findings = lint.lint_file(path)
            self.assertTrue(findings, name)
            self.assertEqual({c for _, c, _ in findings}, {"placeholder"}, name)

    def test_cli_exit_codes(self):
        script = os.path.join(ROOT, "lint_claude_md.py")
        with tempfile.TemporaryDirectory() as tmp:
            good = os.path.join(tmp, "CLAUDE.md")
            with open(good, "w", encoding="utf-8") as fh:
                fh.write(CLEAN)
            res = subprocess.run([sys.executable, script, good], capture_output=True, text=True)
            self.assertEqual(res.returncode, 0)
            self.assertEqual(res.stdout.strip(), "OK")
            bad = os.path.join(tmp, "BAD.md")
            with open(bad, "w", encoding="utf-8") as fh:
                fh.write("# T\n\n## Empty\n")
            res = subprocess.run([sys.executable, script, bad], capture_output=True, text=True)
            self.assertEqual(res.returncode, 1)
            self.assertIn("empty-section", res.stdout)


if __name__ == "__main__":
    unittest.main()
