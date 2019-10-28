# Release process

## Build

```bash
rm dist/*
pipenv run python setup.py sdist
```

## Deploy

```bash
pipenv run twine upload dist/*
```
