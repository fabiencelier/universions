"""Setup universions module."""

from os import path
from setuptools import find_packages, setup


def get_long_description():
    """Read the description from external file."""
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, "README.md"), encoding="utf-8") as file:
        return file.read()


setup(
    name="universions",
    version="0.1.0-dev022",
    author="Fabien Celier",
    author_email="fabien.celier@polytechnique.org",
    packages=find_packages(exclude=["tests"]),
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
)
