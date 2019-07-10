import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nextbike_api",
    version="0.0.1",
    author="Bohdan Dmytriv",
    author_email="bodik75@ukr.net",
    description="Nextbike API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/smthsm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
