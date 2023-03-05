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
