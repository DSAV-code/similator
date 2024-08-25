from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
import subprocess

class BuildDocsCommand(_build_py):
    """Custom command to build the Sphinx documentation."""
    
    def run(self):
        subprocess.check_call(['sphinx-build', '-b', 'html', 'docs/source', 'docs/build'])
        super().run()

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="similator",
    version="0.1.1",
    description="A Python library for validating and comparing text data using bytearrays.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DSAV-code/similator",
    author="Diego San Andrés Vasco",
    author_email="sanandresvascodiego@gmail.com",
    license="GNU General Public License v3.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    extras_require={
        'docs': [
            'sphinx>=4.0',
            'sphinx-rtd-theme',
        ],
        'dev': ['pytest>=8.3.2', 'twine>=5.1.1'],
    },
    python_requires=">=3.8",
    include_package_data=True,
    cmdclass={
        'build_docs': BuildDocsCommand,
    },
)