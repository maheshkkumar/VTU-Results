# VTUResults
Python Package to fetch VTU Results.

| Build Status | Version | Downloads |
| ------------ | ------------- | ------- | ------------------- |
| [![Build Status](https://travis-ci.org/maheshkkumar/VTUResults.svg?branch=master)](https://travis-ci.org/maheshkkumar/VTUResults) | [v1.0.2](https://pypi.python.org/pypi/VTUResults/1.0.1) |[Downloads](https://pypi.python.org/pypi/VTUResults/1.0.1) |


Features
========

- Compatible with Python 2 (2.7+).
- Get Result details for any USN

Installation
========

    $ pip install VTUResults
      If this doesn't work, try switching to root by doing $ sudo pip install VTUresults
      
     (for python 2.6 and above) Sometimes if pip gives any problem (Example : ImportError: cannot import name IncompleteRead) try installion using the python setuptools (check https://pypi.python.org/pypi/setuptools for details about setuptools) as
    $ sudo easy_install VTUResults

Usage
========

    from vr import VR

    result =  VR()

    # print the result the of the USN sent as parameter
    result.get_usn('1XX12XX100')
    
API Reference
========

## Class: `VR`

### Get Result from VTU Results

#### `get_usn`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `usn` | string | Yes | Returns the Result of the USN, passed as the parameter to get_usn function | ------|

Example
========

    from vr import VR
    result =  VR()
    result.get_usn('1XX12XX100')
 



Python Dependencies
========
##### [requests](http://docs.python-requests.org/en/latest/)

    $ pip install requests
     If this doesn't work, try switching to root by doing $ sudo pip install VTUresults
      
     (for python 2.6 and above) Sometimes if pip gives any problem (Example : ImportError: cannot import name IncompleteRead) try installion using the python setuptools (check https://pypi.python.org/pypi/setuptools for details about setuptools) as
    $ sudo easy_install requests
    
Requests is a Python HTTP library, released under the Apache2 License. The goal of the project is to make HTTP requests simpler and more human-friendly.

Requests takes all of the work out of Python HTTP/1.1 — making your integration with web services seamless. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, powered by urllib3, which is embedded within Requests

##### [lxml](http://docs.python-guide.org/en/latest/scenarios/scrape/)

    $ pip install lxml
     If this doesn't work, try switching to root by doing $ sudo pip install VTUresults
      
     (for python 2.6 and above) Sometimes if pip gives any problem (Example : ImportError: cannot import name IncompleteRead) try installion using the python setuptools (check https://pypi.python.org/pypi/setuptools for details about setuptools) as
    $ sudo easy_install lxml

lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.

##### [Easy Install](https://pythonhosted.org/setuptools/easy_install.html)

Easy Install is a python module (easy_install) bundled with setuptools that lets you automatically download, build, install, and manage Python packages. You will need at least Python 2.6. An easy_install script will be installed in the normal location for Python scripts on your platform.
