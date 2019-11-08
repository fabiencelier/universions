set -e # Stop at the first failure

# Black formatting
pipenv run black . --check

# Pylint
pipenv run pylint universions

# Order import with isort
pipenv run isort . --recursive --check-only

# Types with Pyright
yarn run pyright universions

# Tests
pipenv run pytest .