import setuptools

# IMPORTANT: The setup nor pip differentiates packages based on OS
# Simplest blog for whl file creation
# https://dzone.com/articles/executable-package-pip-install

# METADATA, DESCRIPTION

# name, Name of your package.
# version, Current version of your pip package.
# scripts, List of executable files.
#       It's recommended to keep them the same as your pip package name.
#       Here we are using demomain.
# author and author_email, Name and Email Id of the author.
# description, A short description of the package.
# long_description, A description of the package.
# long_description_content_type, A longer description.
#       Here it is markdown.
#       We are picking README.md for the long description.
# packages, Use for other package dependencies.
# classifiers, Contains all the classifiers of your project.

# RUN setup.py with below command
# python3 setup.py bdist_wheel

# whl Can be installed using the following
# python -m pip install dist/testwhl-0.1-py3-none-any.whl

with open("README.md", "r") as fh:
    long_description = fh.read()

# Package project description of .whl file
setuptools.setup(
     name='testwhl',
     version='1.0',
     scripts=['demomain.py'],
     author="Ganesh Bhat",
     author_email="ganesh@ganesh.com",
     description="Demo whl package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)

# The Pypirc file stores the PyPi repository information
# https://docs.python.org/2.5/dist/pypirc.html
# for Windows :  C:\Users\UserName\.pypirc
# for *nix :   ~/.pypirc

# To upload your dist/*.whl file on PyPi https://pypi.org/, use Twine
# python3 -m twine upload dist/*
