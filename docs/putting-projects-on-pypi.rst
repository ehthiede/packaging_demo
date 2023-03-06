Putting Projects On PyPi
========================

Uploading projects to PyPi allow users to install them from the internet with `pip`.
To test that the uploading procedure works, we are going to upload our project to TestPyPi.
TestPyPi is a test version PyPi that can be used to check that the upload is successful.

First, make an account on TestPyPi.  Then, create an api-token with scope set 
to "entire account" and follow the instructions in the section labeled "Using this token".

Once that has been done, install twine and use it to upload your package.

::
    
    pip install --upgrade build twine
    python -m build
    twine upload --repository testpypi dist/*

In order, these commands install the utilities required to build and upload your project,
construct a shareable and executable version of the code,
and then upload that version to the testpypi server.

To test that the code can be installed succesfully, create an empty environment and run

::

    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple [projectname]

Once you have convinced yourself that things are working as intended, 
make an account on PyPi.org and upload
to the actual pypi with

::

    twine upload dist/*

and the package can then be installed using 

::

    pip install [projectname]

