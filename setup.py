from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).resolve().parent
README = (here / "README.md").read_text(encoding="utf-8")
VERSION = (here / "VERSION").read_text(encoding="utf-8").strip()


setup(
    name="kimfame",
    version="0.0.1",
    author="kimfame",
    author_email="renownkim@gmail.com",
    description="PyPI test project",
    long_description=README,
    url="https://github.com/kimfame/kimfame",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)