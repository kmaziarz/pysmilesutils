from setuptools import setup, find_packages

setup(
    name="syntheseus-PySMILESutils",
    version="1.1.0",
    description="Fork of PySMILESutils for use in the syntheseus library",
    license="Apache 2.0",
    packages=find_packages(exclude=("tests",)),
    url="https://github.com/kmaziarz/pysmilesutils",
)
