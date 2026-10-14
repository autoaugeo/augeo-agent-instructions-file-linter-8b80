# CLAUDE.md linter and two sample templates

A small command-line linter for `CLAUDE.md` files, plus two free starter templates (a Python library and a Node.js API).

This project is built and maintained by an automated agent system.

AI-generated content. Independent; not affiliated with or endorsed by Anthropic.

## What the linter checks

`lint_claude_md.py` reads one file and reports a finding for each of these:

- the file is missing, unreadable or empty
- there is no top-level heading (a line starting with `# `)
- a heading has an empty section (headings inside code fences are ignored)
- leftover placeholders: the to-do marker words (the usual four-letter one, FIXME, TBD), angle-bracket stubs such as `<placeholder>` or `<FILL IN`, the text `your-command-here`, and Latin filler text
- no section whose heading names build or test commands (for example "Commands", "Build", "Testing", "Setup")
- a line longer than 200 characters
- a file longer than 300 lines

It exits 1 when there is any finding and prints one line per finding. When the file is clean it prints `OK` and exits 0. A wrong number of arguments exits 2.

## How to run it

Python 3 and the standard library are all you need.

```
python lint_claude_md.py path/to/CLAUDE.md
```

Example output:

```
CLAUDE.md: [no-commands] no section naming build or test commands
CLAUDE.md:7: [placeholder] leftover placeholder '<FILL IN'
```

Findings that apply to the whole file print the path without a line number and sort first.

Run the tests:

```
python -m unittest discover -s tests
```

## The two templates

- `templates/python-library.md`
- `templates/node-api.md`

Copy one to the root of your project as `CLAUDE.md`, then replace every `<FILL IN: ...>` with your own value, delete the hints, and remove sections that do not apply. Run the linter on the result. While placeholders remain, the linter reports only `placeholder` findings for these templates; when you have filled them all in, it prints `OK`.

## Paid kit

A separate paid kit of 8 CLAUDE.md templates (9 files in its zip) is sold on Gumroad by the same project. It is not part of this repository, and the linter and the 2 templates here are free and complete without it.

## License

MIT. See `LICENSE`.
