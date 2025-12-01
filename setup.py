from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys
import pathlib

starter_packages = [
    # generic dependencies
    "nltk",
    "numpy",
    "tqdm",
    "pandas",
    "termcolor",
    "scikit-learn",
    "seaborn",
    "beautifulsoup4",
    "gspread",
    "oauth2client",
    "lxml",
    "wget",
    "flask",
    "ipython"
]

setup(
    name='opp115',
    version='0.1',
    packages=find_packages(),
    install_requires=starter_packages,
)
