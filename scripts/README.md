Purpose
- Provide a lightweight local pre-commit hook to run basic Django checks before committing.

Install (local repo)
- Copy and enable the hook in your local repo's git hooks directory:

```bash
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

- Or create a symlink so the hook stays in sync:

```bash
ln -s ../../scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

What the hook does
- Runs `python manage.py check` to execute Django system checks.
- Runs `python manage.py makemigrations --check --dry-run` to detect model changes missing migrations.
- Optionally runs `flake8` if it's installed in your environment.

Notes
- This hook runs locally only; it does not affect remote CI. Consider adding a CI workflow if you want remote checks.
- If you use a virtualenv, ensure you activate it before committing or use the full Python path in the script.
