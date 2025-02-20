from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="snelnotuleren-sdk",
    version="0.1.0",
    author="Niels van der Werf",
    author_email="niels@snelnotuleren.nl",
    description="Official Python SDK for the Snelnotuleren API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snelnotuleren/python-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0"
    ],
    license="MIT",
)
