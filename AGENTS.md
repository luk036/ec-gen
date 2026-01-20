# ec-gen - Agent Development Guide

## Build Commands

```bash
# Build the package (sdist + wheel)
python -m build

# Or using tox
tox -e build

# Clean build artifacts
tox -e clean
```

## Test Commands

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_combin.py

# Run specific test function
pytest tests/test_combin.py::test_comb_with_various_inputs

# Run with coverage
pytest --cov=ec_gen --cov-report=term-missing

# Run tests using tox
tox
```

## Code Style

### Formatting
- **Black** (v23.7.0) - Apply with: `black src/ tests/`
- **isort** (profile=black) - Apply with: `isort src/ tests/`
- Line length: 256 characters (flake8-compatible Black settings)

### Linting
- **flake8** with max_line_length=256, ignores E203 and W503
- Run all linting checks: `pre-commit run --all-files`

### Type Checking
- **mypy** (Python 3.12 target)
- Configuration: `mypy.ini`
- Run with: `mypy src/ec_gen/`

## Code Conventions

### Project Structure
- **Source layout**: `src/ec_gen/` (not flat layout)
- **Tests**: `tests/` directory, matching source structure
- **Package name**: `ec_gen` (underscore, not hyphen)

### Naming
- **Functions/variables**: snake_case (e.g., `fib`, `emk_comb_gen`, `val_a`)
- **Constants**: UPPER_CASE (standard convention)
- **Private items**: underscore prefix (e.g., `_logger`)

### Imports
- Group order: stdlib → third-party → first-party (ec_gen)
- No wildcard imports (`from x import *` forbidden)
- isort will automatically sort (profile=black, known_first_party=ec_gen)

### Type Hints
- Required for all function signatures
- Use `Generator[T, None, None]` for generators, not just `Generator`
- Type-checking enabled via mypy

### Docstrings
- Google-style or Sphinx-compatible format
- Include parameter types, return types, and examples
- All modules/functions should have docstrings

### Error Handling
- Use `assert` for internal invariants (e.g., `assert n > 0`)
- Use `pytest.raises()` for testing expected exceptions
- Avoid bare `except:` blocks

### Testing
- Use pytest fixtures (e.g., `capsys`, `monkeypatch`)
- Test both normal and edge cases
- Include doctests in docstrings for simple functions
- Use `if __name__ == "__main__": import doctest; doctest.testmod()` pattern

### Pre-commit Hooks
Pre-commit runs automatically on commit (if installed):
```bash
pre-commit install
pre-commit run --all-files  # Manual run
```

## Notes
- This is a PyScaffold 4.5 project
- Python 3.12 target version (see mypy.ini)
- Package uses `setuptools_scm` for versioning
- Tests run on commit via GitHub Actions
