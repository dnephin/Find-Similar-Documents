#!/bin/bash
python setup.py build_ext --inplace && cp ./*.so ../src/
