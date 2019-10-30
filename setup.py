"""Setup universions module."""

from setuptools import find_packages, setup

setup(
    name="universions",
    version="0.1.0-dev021",
    author="Fabien Celier",
    author_email="fabien.celier@polytechnique.org",
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/fabiencelier/universions",
    keywords=["version", "versions", "universal"],
    license="LICENSE.txt",
    description="Get version of other tools.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
