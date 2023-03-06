# Code for performing weighted backprojection
[![](https://github.com/ehthiede/packaging_demo/actions/workflows/testing.yml/badge.svg)](https://github.com/ehthiede/packaging_demo/actions)

Installation
-----------------
To install, run 
```shell
    pip install -e .
```
in this directory.

Running the Code
-----------------
The weighted backprojection can be imported in your python files as 
```Python
    import wbpj.weighted_backprojection_1d
    volume = weighted_backprojection_1d(images, angles)
```
If images are equispaced, then the command line interface can also be used,
```shell
    python -m wbpj.perform_reconstruction image_file.ny 0 172 --degrees
```

Running the Tests
-----------------
Tests can be run in your current environment using pytest,
```shell
    pytest tests/
```
