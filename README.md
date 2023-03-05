# Code for performing weighted backprojection

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
Tests can also be run installed into a fresh environment using tox by running 
```shell
    tox
```
in this directory.