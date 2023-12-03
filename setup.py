import os

from setuptools import setup

requirements = ["olefile", "pyzipper", "yara-python", "pefile", "peutils"]

# build console_scripts list automatically
modules = [module for module in os.listdir("./src") if module.endswith(".py") and module != "__init__.py"]
console_scripts = [f"{module.replace('_', '-')} = src.{module.replace('.py', '')}:Main" for module in modules]

setup(
    name="ds-pip",
    description="Make several Didier Stevens tools installable via pip",
    version="2.1.2",
    author="Tariq Alashaikh",
    url="https://github.com/illbison/ds-pip",
    python_requires=">=3.8",
    install_requires=requirements,
    packages=["src", "src.lib"],
    entry_points={
        "console_scripts": console_scripts,
    },
)
