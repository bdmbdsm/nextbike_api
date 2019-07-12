import os
import sys
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

setuptools.setup(
    name="nextbike_api",
    version="1.0.0",
    author="Bohdan Dmytriv",
    author_email="bodik75@ukr.net",
    description="Nextbike API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bdmbdsm/nextbike_api",
    packages=setuptools.find_namespace_packages(exclude=['tests']),
    install_requires=['requests==2.22.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
