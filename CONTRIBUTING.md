# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the `GPLv3 license` and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

## How to report a bug

Report bugs on the Issue Tracker.

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

## How to request a feature

Request features on the Issue Tracker.

## How to set up your development environment

You need Python 3.8+ and the following tools:

- pdm

Clone the submodules:

```bash
git submodule update --init
```

Install the package with development requirements:

```bash
pdm install
```

## How to test the project

Run the full test suite:

```bash
pdm run test
```

Unit tests are located in the ``tests`` directory,
and are written using the [pytest](https://pytest.readthedocs.io/) testing framework.

## How to submit changes

Open a `pull request` to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before committing your change, you can install pre-commit as a Git hook by running the following command:

```bash
pdm run lint
```

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.
