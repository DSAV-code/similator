# Installation Guide

This guide will help you install the **Similator** library and get it up and running in no time. Follow the steps below to set up the environment and install the necessary dependencies.

## Prerequisites

Before installing Similator, ensure that you have the following installed:

- **Python 3.8+**: Similator requires Python version 3.8 or higher. You can download Python from the [official website](https://www.python.org/downloads/).

To verify the installation of Python, run the following command:

```bash
python --version
```

## Installing Similator

Similator is distributed as a Python wheel package that includes both Python and Rust functionalities, compiled and ready to use. This means users do **not** need to have Rust installed to use Similator.

To install Similator, you can use `pip`, the Python package manager. Run the following command in your terminal:

```bash
pip install similator
```

This will install the latest version of Similator from [PyPI](https://pypi.org/project/similator).

## Verifying the Installation

After installation, you can verify that Similator is installed correctly by running:

```bash
python -c "import similator; print(similator.__version__)"
```

This should print the installed version of Similator.

## For Developers: Building from Source

If you are interested in contributing to Similator or building the package from source, you will need to install **Rust** and **Maturin**.

- **Rust**: Install Rust by following the instructions on the [official Rust website](https://www.rust-lang.org/tools/install).
- **Maturin**: Install Maturin by running `pip install maturin`.

To build the wheel package locally, run:

```bash
maturin build
```

This will create a wheel file that can be installed using `pip`.

## Troubleshooting

If you encounter any issues during installation:

- Ensure that Python is correctly installed and accessible from your command line.
- Check that `pip` is up to date by running `pip install --upgrade pip`.
- If you still face issues, please refer to the [GitHub Issues](https://github.com/DSAV-code/similator/issues) page to report the problem or seek help.

## Next Steps

Once Similator is installed, you can proceed to the [Usage](usage.md) section to learn how to use its features. 

If you're interested in contributing to the project, feel free to head over to the [Contribution](contributing.md) section for more details.
