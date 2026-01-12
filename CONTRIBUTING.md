# HighBar Contributing Guidelines

Thank you for your interest in contributing to HighBar! This document provides guidelines for contributing to the project.

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HighBar.git
   cd HighBar
   ```
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Code Style

- Follow PEP 8 guidelines
- Use type hints for function signatures
- Format code with `black`:
  ```bash
  poetry run black highbar tests
  ```
- Lint with `ruff`:
  ```bash
  poetry run ruff check highbar tests
  ```
- Type check with `mypy`:
  ```bash
  poetry run mypy highbar
  ```

## Testing

- Write tests for all new features
- Ensure all tests pass:
  ```bash
  poetry run pytest
  ```
- Maintain test coverage above 80%:
  ```bash
  poetry run pytest --cov=highbar --cov-report=term-missing
  ```

## Commit Messages

Use clear, descriptive commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/changes
- `refactor:` for code refactoring
- `chore:` for maintenance tasks

Example: `feat: add support for custom citation formats`

## Pull Requests

1. Ensure all tests pass
2. Update documentation if needed
3. Add a clear description of changes
4. Reference any related issues
5. Request review from maintainers

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Report unacceptable behavior to maintainers

## Questions?

Feel free to open an issue for any questions or concerns.
