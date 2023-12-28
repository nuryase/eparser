import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eParser",
    version="0.1.0",
    author="yasen",
    description="Library for EPUB handling and parsing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nuryase/eparser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
