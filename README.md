![VTU Results](https://raw.github.com/maheshkkumar/VTUResults/master/vtu.jpg)

# VTUResults
Python Package to fetch [VTU](http://results.vtu.ac.in) Results.

| Build Status | Dependency Status | Version | License | Downloads |
| ------------ | ------------- | ------- | -------------------|--------------- |
| [![Build Status](https://travis-ci.org/maheshkkumar/VTUResults.svg?branch=master)](https://travis-ci.org/maheshkkumar/VTUResults) | [![Dependency Status](https://gemnasium.com/maheshkkumar/VTUResults.svg)](https://gemnasium.com/maheshkkumar/VTUResults) | [![Foo](https://img.shields.io/badge/version-v2.0.1-blue.svg)](https://pypi.python.org/pypi/VTUResults/2.0.1) | [![GitHub license](https://img.shields.io/badge/license-GPLv2-blue.svg)](https://raw.githubusercontent.com/maheshkkumar/VTUResults/master/LICENSE) |[![Foo](https://img.shields.io/badge/downloads-6k%2Fmonth-blue.svg)](https://pypi.python.org/pypi/VTUResults/2.0.1) |





Features
========

- Compatible with Python 2 (2.7+)
- Get Result details for any USN
- All the results will be exported to a .txt file in the current working directory
- In `get_entire_result` method, `rank_list.txt` and `result_class.txt` will be created, the former file will contain the rank list of all the students and the latter file will contain the entire result data of all the students.
- In `get_group_usn` method, `results.txt` will be created in the current working directory, this file will contain all the result data of your chosen USN.
- In `get_usn` method, `result.txt` will be created and it will contain the result of a single USN.

Installation
========

    $ sudo pip install VTUResults

Usage
========

    from vr import VR

    result =  VR()

    # print the result of the USN sent as parameter to get_usn method.
    result.get_usn('1XX12XX100')
    result.get_group_usn()
    result.get_entire_result()
    
    Every result will be exported to a text file in your current working directory.
    
    
Package Reference
========

## Class: `VR`

### Get Result from VTUResults

#### `get_usn(usn)`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `usn` | string | Yes | Returns the Result of the USN, passed as the parameter to get_usn function | `None` |

#### `get_group_usn()`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `None` | `None`  |  `No` | Returns the Result of the total number of USN entered through terminal| `None` |

#### `get_entire_result()`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `None` | `None`  | `No`  | Returns the Result of the entire department| `None` |



Example
========

    from vr import VR
    result =  VR()
    result.get_usn('1XX12XX100')
    result.get_group_usn()
    result.get_entire_result()
    
    # get_entire_result method will create a rank_file.txt in your current working directory, this file contains the rank list of all the students with their respective total marks.



Python Dependencies
========
##### [requests](http://docs.python-requests.org/en/latest/)

    $ sudo pip install requests

Requests is a Python HTTP library, released under the Apache2 License. The goal of the project is to make HTTP requests simpler and more human-friendly.

Requests takes all of the work out of Python HTTP/1.1 — making your integration with web services seamless. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, powered by urllib3, which is embedded within Requests

##### [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/)

    $ sudo pip install beautifulsoup4

Beautiful Soup is a Python library designed for quick turnaround projects like screen-scraping.

