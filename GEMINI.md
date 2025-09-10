# GEMINI.md

## Project Overview

This is a Python library for "Enumerative Combinatoric Generation". The project is set up using PyScaffold, a tool for bootstrapping Python projects. It uses `setuptools` for packaging and `tox` for task automation.

The library's source code is located in the `src/ec_gen` directory. The project includes a suite of tests in the `tests` directory.

## Building and Running

### Dependencies

The project's dependencies are managed in the `requirements` directory, with `default.txt` for runtime dependencies and `test.txt` for testing dependencies.

To install the dependencies, you can run:

```bash
pip install -r requirements/default.txt
pip install -r requirements/test.txt
```

### Testing

The project uses `pytest` for testing. You can run the tests using `tox`:

```bash
tox
```

This will run the tests in an isolated environment, as defined in `tox.ini`.

### Building

To build the project, you can use the `build` environment in `tox`:

```bash
tox -e build
```

This will create a distributable package in the `dist` directory.

## Development Conventions

### Code Style

The project uses `black` for code formatting and `isort` for sorting imports. It also uses `flake8` for linting. These tools are configured as pre-commit hooks in `.pre-commit-config.yaml`.

To ensure your code adheres to the project's style, you should install the pre-commit hooks:

```bash
pre-commit install
```

### Contributing

The `CONTRIBUTING.md` file provides guidelines for contributing to the project. It is recommended to read it before making any contributions.
