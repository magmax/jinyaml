from setuptools import setup

import jinyaml


def read_description():
    with open("README.rst") as fd:
        return fd.read()


setup(
    name="sphinx-jinyaml",
    version=jinyaml.__version__,
    # long_description=read_description(),
    description="Plugin for sphinx to use Jinja in documents",
    url="https://github.com/magmax/sphinx-jinyaml",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Framework :: Sphinx :: Extension",
    ],
    install_requires=["docutils>=0.11", "sphinx>=1.3.1"],
    extras_require={"markdown": ["commonmark>=0.8.1"]},
    packages=["jinyaml"],
)
