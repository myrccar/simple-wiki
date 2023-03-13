import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplewiki",
    version="1.0.0",
    author="sami joseph",
    author_email="4myrccar@gmail.com",
    description="a package to simplify the wikipedia api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myrccar/simple-wiki",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10.0',
)
