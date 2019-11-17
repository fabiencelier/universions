# Contributing

## Install

Requirements:

- pipenv
- yarn

Install python dependencies :
`pipenv install --dev --python 3.8`

Install yarn dependencies :
`yarn install`

## Before a pull request :

Run the checks :
`./scripts/check.sh`

## Contribute a new tool

If you want to add a new tool to universions here are all the steps :

- create a new module universions/XXX
- define the logic to get the version.
- check online to find all the vali version number of your tool, including prereleases.
- test it in tests/test_XXX_version.py
- add a CLI entry in universions/cli.py
- Add your tool in the README.md list
