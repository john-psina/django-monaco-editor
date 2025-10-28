# Contributing to Django Monaco Editor

Thank you for your interest in contributing! 🎉

## 🚀 Quick Start

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/john-psina/django-monaco-editor.git
   cd django-monaco-editor
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -e .
   pip install black flake8 isort
   ```

5. **Create a branch:**
   ```bash
   git checkout -b feat/your-feature-name
   ```

## 📝 Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/) for automated versioning and changelog generation.

### Format
```
<type>: <description>

[optional body]

[optional footer]
```

### Types
- `feat:` - New feature (triggers minor version bump)
- `fix:` - Bug fix (triggers patch version bump)
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `perf:` - Performance improvements
- `test:` - Adding or updating tests
- `build:` - Build system changes
- `ci:` - CI/CD changes
- `chore:` - Other changes

### Examples
```bash
git commit -m "feat: add support for custom themes"
git commit -m "fix: resolve editor crash on empty content"
git commit -m "docs: update installation instructions"
```

### Breaking Changes
```bash
git commit -m "feat!: redesign widget API

BREAKING CHANGE: MonacoField constructor parameters have changed"
```

## 🧪 Testing

### Test your changes locally:
```bash
# Navigate to sandbox
cd sandbox

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit `http://localhost:8000/admin/` and test the Monaco Editor fields.

## 🎨 Code Style

We use:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting

### Format your code:
```bash
black django_monaco_editor/
isort django_monaco_editor/
flake8 django_monaco_editor/
```

## 📤 Submitting a Pull Request

1. **Ensure your code follows the style guide**
2. **Write clear commit messages** using conventional commits
3. **Push your branch:**
   ```bash
   git push origin feat/your-feature-name
   ```
4. **Create a Pull Request** on GitHub
5. **Fill out the PR template**
6. **Wait for review**

### PR Title Format
PR titles should also follow conventional commits:
```
feat: add dark mode support
fix: resolve memory leak in editor
```

## 🐛 Reporting Bugs

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md) when creating an issue.

Include:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Django version, Python version, etc.)
- Code samples and error logs

## 💡 Suggesting Features

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md).

Include:
- Clear description of the feature
- Use case and benefits
- Code examples of how it would work

## 📜 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

## 🎯 Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🧪 Test coverage
- 🌐 Internationalization
- 🎨 UI/UX improvements
- ⚡ Performance optimizations

## ❓ Questions?

Feel free to open an issue with the `question` label or start a discussion.

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🙏

