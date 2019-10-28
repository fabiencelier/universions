from distutils.core import setup

setup(
    name="universions",
    version="0.1.0-dev01",
    author="Fabien Celier",
    author_email="fabien.celier@polytechnique.org",
    packages=["universions", "universions.java"],
    url="https://github.com/fabiencelier/universions",
    keywords=["version", "versions", "universal"],
    license="LICENSE",
    description="Get version of other tools.",
    install_requires=["Python >= 3.7"],
)
