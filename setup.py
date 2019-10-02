from os import environ as env
from setuptools import find_packages, setup
from setuptools.command.install import install
import sys

VERSION = "0.1.0"

with open("README.md", "r", encoding="utf-8") as rdm:
    long_description = rdm.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = env .get('CLIPENV_TAG')
        if tag != VERSION:
            info = f"Git tag: {tag} doesn't match with this version: {VERSION}"
            sys.exit(info)


setup(
    name="clipenv",
    version=VERSION,
    description="Attach your venv variables with a clip to your project",
    long_description=long_description,
    author="Ana Valeria Calderón Briz, Daniel Omar Vergara Pérez",
    author_email="valerybriz@gmail.com, daniel.omar.vergara@gmail.com",
    url="https://github.com/dany2691/clipenv",
    license="MIT",
    install_requires=[
        "click",
        "colored"
    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    packages=find_packages(exclude=('tests',)),
    entry_points={
        "console_scripts": [
            "clipenv=clipenv.__main__:clipenv"
        ]
    },
    cmdclass={'verify': VerifyVersionCommand}
)
