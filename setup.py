from setuptools import setup

setup(
    name='pkg_private_test',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:ynshen/pkg_private_test.git',
    author='Yuning Shen',
    author_email='ynshen23@gmail.com',
    license='unlicense',
    packages=['pkg_prvt_test'],
    zip_safe=False
)
