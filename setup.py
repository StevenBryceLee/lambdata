"""lambdata - a collection of helper functions
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open('README.md','r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='lambdata-StevenBryceLee',
    version = '0.0.5',
    author = 'StevenBryceLee',
    description = 'A collection of helper functions',
    long_description = LONG_DESCRIPTION,
    long_description_content = 'text/markdown',
    url = 'https://github.com/StevenBryceLee/lambdata/',
    packages = setuptools.find_packages(),
    python_requires = '>=3.6',
    install_requires = REQUIRED,
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',

    ]
)