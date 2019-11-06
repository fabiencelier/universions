"""Setup universions module."""

from os import path

from setuptools import find_packages, setup


def get_long_description():
    """Read the description from external file."""
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, "README.md"), encoding="utf-8") as file:
        return file.read()


def get_package_version():
    """Read the version of the package.
    See https://packaging.python.org/guides/single-sourcing-package-version
    """
    version_exports = {}
    file_directory = path.abspath(path.dirname(__file__))
    with open(path.join(file_directory, "universions", "_version.py")) as file:
        exec(file.read(), version_exports)  # pylint: disable=exec-used
    return version_exports["VERSION"]


setup(
    name="universions",
    version=get_package_version(),
    author="Fabien Celier",
    author_email="fabien.celier@polytechnique.org",
    packages=find_packages(exclude=["test"]),
    url="https://github.com/fabiencelier/universions",
    keywords=["version", "versions", "universal"],
    license="LICENSE.txt",
    description="Get version of other tools.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["universions = universions:cli"]},
)
