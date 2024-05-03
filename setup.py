from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = "AuthSys is a Python library Allows you to create a membership system, so you add keys to your tools."

LONG_DESCRIPTION = """
AuthSys is a Python library designed to simplify Membership processes. With AuthSys, you can easily integrate secure user authentication and registration functionalities into your Python applications.

## Key Features:
- **Simple Integration**: Easily integrate user authentication and registration functionalities into your Python projects.
- **Secure Authentication**: Securely authenticate users using keys and access tokens.
- **User Registration**: Register new users with customizable registration times.
- **User Management**: Edit user information and remove users from your system.

For more information, please visit the [GitHub repository](https://github.com/IceBytes/AuthSys). 
"""


setup(
    name="AuthSys",
    version=VERSION,
    author="Just Ice",
    author_email="MrAws.developer@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=["AuthSys", "Membership", "Python library"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url='https://github.com/IceBytes/AuthSys/',
    project_urls={
        'Source': 'https://github.com/IceBytes/AuthSys/',
        'Bug Reports': 'https://github.com/IceBytes/AuthSys/issues',
        'Documentation': 'https://github.com/IceBytes/AuthSys/'
    },
)
