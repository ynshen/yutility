#!/bin/bash

python setup.py bdist_wheel
pip uninstall yuning-util
MB_PKG=$(ls -t dist/*.whl | head -1)
pip install $MB_PKG
