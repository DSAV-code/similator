# Contributing to Similator

We welcome contributions to **Similator**! Whether it's fixing bugs, improving documentation, or adding new features, your contributions are greatly appreciated. Follow the guidelines below to get started.

## Getting Started

To contribute to Similator, you will need to set up the development environment. Follow these steps:

### 1. Fork the Repository

1. Visit the [Similator GitHub repository](https://github.com/DSAV-code/similator).
2. Click on the "Fork" button in the upper-right corner of the page.
3. This creates a copy of the repository under your GitHub account.

### 2. Clone Your Fork

Clone your forked repository to your local machine:

```bash
git clone https://github.com/DSAV-code/similator.git
cd similator
```

### 3. Install Development Dependencies

Similator uses `Maturin` to build the Rust code and `pytest` for testing. You will need to install these dependencies:

- **Python**: Ensure you have Python 3.8+ installed.
- **Rust**: Install Rust by following the instructions on the [official Rust website](https://www.rust-lang.org/tools/install).
- **Maturin**: Install Maturin by running:

    ```bash
    pip install similator[dev]
    ```

### 4. Build the Project

Build the Python package, which includes compiling the Rust code:

```bash
maturin develop
```

This will build the package and install it in your local environment for development purposes.

### 5. Run Tests

To ensure everything is set up correctly, run the test suite using `pytest`:

```bash
pytest
```

All tests should pass without errors. If any tests fail, try to resolve the issues before proceeding.

## Contribution Guidelines

### 1. Create a Branch

Create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Edit the code and make the necessary changes. Make sure to write or update tests for your code.

### 3. Format Your Code

Ensure your code follows the project's coding style. You can use tools like `black` and `flake8` to format and lint your code:

```bash
black .
flake8 .
```

### 4. Commit Your Changes

Once you're satisfied with your changes, commit them:

```bash
git add .
git commit -m "Add a brief description of your changes"
```

### 5. Push to Your Fork

Push your branch to your forked repository:

```bash
git push origin feature/your-feature-name
```

### 6. Submit a Pull Request

1. Go to the original repository on GitHub.
2. Click on the "Compare & pull request" button.
3. Provide a descriptive title and summary for your pull request.
4. Submit the pull request for review.

## Code Review Process

- One or more maintainers will review your pull request. Feedback may be provided, and you may be asked to make some changes.
- Once your changes are approved, your pull request will be merged into the main branch.

## Reporting Issues

If you find a bug or have a feature request, please open an issue on the [GitHub Issues](https://github.com/DSAV-code/similator/issues) page. Make sure to provide as much detail as possible to help us understand and reproduce the issue.

## Thank You for Contributing!

Your contributions help make **Similator** better for everyone. Thank you for taking the time to contribute!