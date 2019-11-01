# Release process

## Deploy on pypi

### Build

```bash
rm dist/*
pipenv run python setup.py sdist
```

### Deploy

```bash
pipenv run twine upload dist/*
```

## Documentation

```bash
cd docs
pipenv run sphinx-apidoc -o source/pydoc ../universions
pipenv run make html
```
