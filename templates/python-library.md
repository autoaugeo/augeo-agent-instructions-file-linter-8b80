# CLAUDE.md: Python library

Fill in each <FILL IN>, delete the hint in parentheses, and remove any section that does not apply. Aim to stay under 200 lines.

## Project overview

- Name: <FILL IN: package name as on PyPI>
- Purpose: <FILL IN: one sentence on what the library does and for whom>
- Python versions supported: <FILL IN: e.g. 3.10 to 3.13>
- Public API lives in: <FILL IN: e.g. src/mylib/__init__.py>
- Packaging: <FILL IN: e.g. pyproject.toml with hatchling, setuptools or poetry>

## Commands

- Install for development: `<FILL IN: e.g. pip install -e ".[dev]">`
- Run all tests: `<FILL IN: e.g. pytest -q>`
- Run one test file: `<FILL IN: e.g. pytest tests/test_parser.py -q>`
- Lint: `<FILL IN: e.g. ruff check .>`
- Format: `<FILL IN: e.g. ruff format .>`
- Type check: `<FILL IN: e.g. mypy src>`
- Build distribution: `<FILL IN: e.g. python -m build>`

## Code style

- Formatter and linter config is in <FILL IN: e.g. pyproject.toml>; do not hand-format against it.
- Type hints on every public function and method.
- Docstring style: <FILL IN: Google, NumPy or reST>. Public functions get a docstring.
- Naming: `snake_case` for functions and variables, `PascalCase` for classes.
- Line length: <FILL IN: e.g. 100>.
- Imports: absolute imports inside the package; standard library, third party, then local.

## Directory map

- `src/<FILL IN: package>/`: library code.
- `tests/`: pytest tests that mirror the package layout.
- `docs/`: <FILL IN: docs tool, or delete this line>.
- `pyproject.toml`: metadata, dependencies, tool settings.
- <FILL IN: any other directory Claude must know, e.g. `examples/`>

## Do

- Keep the public API small; export new names in `__init__.py` on purpose.
- Add or update a test with every behaviour change.
- Raise specific exceptions with a helpful message.
- Keep runtime dependencies to a minimum: <FILL IN: allowed dependencies, or "ask before adding any">.
- Preserve backward compatibility of the public API: <FILL IN: your deprecation policy>.

## Don't

- Don't edit generated files: <FILL IN: paths, or delete this line>.
- Don't add a dependency without asking first.
- Don't use bare `except:` or swallow errors silently.
- Don't import from private modules of other packages.
- Don't change version numbers; releases are handled by <FILL IN: person, tool or workflow>.

## Testing

- Framework: <FILL IN: e.g. pytest>.
- Test files are named `test_<module>.py`; test functions start with `test_`.
- Prefer small unit tests with plain asserts; use fixtures for shared setup.
- Network and filesystem access in tests: <FILL IN: e.g. mock network, use tmp_path>.
- Before saying a task is done, run: `<FILL IN: e.g. ruff check . && mypy src && pytest -q>`

## Commit and PR conventions

- Commit message format: <FILL IN: e.g. Conventional Commits "fix(parser): handle empty input">.
- One logical change per commit.
- Branch names: <FILL IN: e.g. feature/short-name>.
- Update `CHANGELOG.md` for user-visible changes: <FILL IN: yes or no, and format>.

## Known gotchas

- <FILL IN: a surprise that cost you time, e.g. "tests need the C extension built first">
- <FILL IN: a second gotcha, or delete this line>

---
AI-generated. Checked only by an automated script. Independent product, not affiliated with or endorsed by Anthropic.
