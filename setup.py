from distutils import sysconfig
from setuptools import setup, Extension, find_packages
import os
import sys
import setuptools
from copy import deepcopy

from pathlib import Path
this_directory = Path(__file__).parent

setup(
    name="dame",
    install_requires=[
        "scipy>=0.18.0",
        "numpy>=1.12",
        "scikit-learn>=0.23",
        "joblib>=1.1.0",
        "matplotlib>=2.0.0",
        "pytest>=6.2.5",
    ],
    version="0.0.5",
    license="MIT",
    author="Hugo RICHARD",
    description="DAME",
    packages=find_packages(),
    python_requires=">=3",
)
