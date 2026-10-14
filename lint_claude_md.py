#!/usr/bin/env python3
"""Lint a CLAUDE.md file. Standard library only.

Usage: python lint_claude_md.py PATH

Prints one finding per line as "PATH:LINE: [code] message" and exits 1 if
there is any finding. Prints "OK" and exits 0 when the file is clean.
"""

import re
import sys

MAX_LINE_LENGTH = 200
MAX_LINES = 300

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b"),
    re.compile(r"\bFIXME\b"),
    re.compile(r"\bTBD\b"),
    re.compile(r"<\s*placeholder[^>]*>", re.IGNORECASE),
    re.compile(r"<\s*FILL IN", re.IGNORECASE),
    re.compile(r"your-command-here", re.IGNORECASE),
    re.compile(r"lorem ipsum", re.IGNORECASE),
]

COMMAND_HEADING = re.compile(
    r"command|build|test|run|install|setup|develop|workflow|script",
    re.IGNORECASE,
)
HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def parse_headings(lines):
    """Return a list of (index, level, title), skipping fenced code blocks."""
    headings = []
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if m:
            headings.append((i, len(m.group(1)), m.group(2)))
    return headings


def lint_text(text):
    """Return a list of (line_number, code, message). Line 0 means whole file."""
    findings = []
    if not text.strip():
        return [(0, "empty", "file is empty")]

    lines = text.splitlines()
    headings = parse_headings(lines)

    if not any(level == 1 for _, level, _ in headings):
        findings.append((0, "no-title", "no top-level heading (a line starting with '# ')"))

    for n, (idx, level, title) in enumerate(headings):
        end = len(lines)
        for nidx, nlevel, _ in headings[n + 1:]:
            if nlevel <= level:
                end = nidx
                break
        if not any(line.strip() for line in lines[idx + 1:end]):
            findings.append((idx + 1, "empty-section", "heading '%s' has an empty section" % title))

    for i, line in enumerate(lines):
        for pattern in PLACEHOLDER_PATTERNS:
            m = pattern.search(line)
            if m:
                findings.append((i + 1, "placeholder", "leftover placeholder '%s'" % m.group(0)))
                break

    if not any(COMMAND_HEADING.search(title) for _, _, title in headings):
        findings.append((0, "no-commands", "no section naming build or test commands"))

    for i, line in enumerate(lines):
        if len(line) > MAX_LINE_LENGTH:
            findings.append((i + 1, "long-line", "line has %d characters (max %d)" % (len(line), MAX_LINE_LENGTH)))

    if len(lines) > MAX_LINES:
        findings.append((0, "long-file", "file has %d lines (max %d)" % (len(lines), MAX_LINES)))

    findings.sort(key=lambda f: f[0])
    return findings


def lint_file(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except FileNotFoundError:
        return [(0, "missing", "file not found")]
    except (OSError, UnicodeDecodeError) as exc:
        return [(0, "unreadable", "cannot read file: %s" % exc)]
    return lint_text(text)


def main(argv):
    if len(argv) != 2:
        print("usage: python lint_claude_md.py PATH", file=sys.stderr)
        return 2
    path = argv[1]
    findings = lint_file(path)
    if not findings:
        print("OK")
        return 0
    for line, code, message in findings:
        where = "%s:%d" % (path, line) if line else path
        print("%s: [%s] %s" % (where, code, message))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
