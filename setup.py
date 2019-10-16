from setuptools import setup

import jinyaml

setup(
    name="jinyaml",
    version=jinyaml.__version__,
    description=(),
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
