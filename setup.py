"""Setup for yutility
See: https://github.com/ynshen/yutility
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yutility',
    version='0.6.3',
    description='Utility functions for development',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ynshen/yutility/',
    author='Yuning Shen',
    author_email='ynshen23@gmail.com',
    keywords='development utility',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/ynshen/yutility/issues/',
        'Source': 'https://github.com/ynshen/yutility/',
    },
)
