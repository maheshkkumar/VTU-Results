![VTU Results](https://raw.github.com/maheshkkumar/VTUResults/master/vtu.jpg)

# VTUResults
Python Package to fetch [VTU](http://results.vtu.ac.in) Results.

| Build Status | Dependency Status | Version | Downloads |
| ------------ | ------------- | ------- | ------------------- |
| [![Build Status](https://travis-ci.org/maheshkkumar/VTUResults.svg?branch=master)](https://travis-ci.org/maheshkkumar/VTUResults) | [![Dependency Status](https://gemnasium.com/maheshkkumar/VTUResults.svg)](https://gemnasium.com/maheshkkumar/VTUResults) | [v1.0.5](https://pypi.python.org/pypi/VTUResults/1.0.5) | [Downloads](https://pypi.python.org/pypi/VTUResults/) |



Features
========

- Compatible with Python 2 (2.7+).
- Get Result details for any USN

Installation
========

    $ pip install VTUResults

Usage
========

    from vr import VR

    result =  VR()

    # print the result of the USN sent as parameter to get_usn method.
    result.get_usn('1XX12XX100')
    
Package Reference
========

## Class: `VR`

### Get Result from VTUResults

#### `get_usn(usn)`

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

Requests is a Python HTTP library, released under the Apache2 License. The goal of the project is to make HTTP requests simpler and more human-friendly.

Requests takes all of the work out of Python HTTP/1.1 — making your integration with web services seamless. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, powered by urllib3, which is embedded within Requests

##### [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/)

    $ pip install beautifulsoup4

Beautiful Soup is a Python library designed for quick turnaround projects like screen-scraping.

