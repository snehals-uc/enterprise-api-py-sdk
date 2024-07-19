# coding: utf-8

import os
from setuptools import setup, find_packages  # noqa: H301

here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "unicourt"
VERSION = os.getenv("SDK_VERSION")
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Python bindings for the UniCourt Enterprise APIs",
    author="UniCourt",
    author_email="support@unicourt.com",
    license="",
    url="https://unicourt.com/",
    project_urls={
        "Source": "https://github.com/UniCourt/enterprise-api-py-sdk/tree/main",
        "Documentation": "https://docs.unicourt.com/",
    },
    keywords=["UniCourt", "UniCourt Python Package",
              "UniCourt Enterprise APIs"],
    python_requires=PYTHON_REQUIRES,
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""The UniCourt Python Package provides simplified access to the UniCourt API for applications written in the Python programming language. Documentation of UniCourt's APIs can be found at docs.unicourt.com. API keys can be obtained by filling out the form here https://unicourt.com/contact-us/?c=sales&enterprise=1
    """,  # noqa: E501
    package_data={"unicourt": ["py.typed"]},
)
