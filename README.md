# Anyway SDK ![Build Status](https://travis-ci.org/hasadna/anyway-sdk-python.png) [![Build status](https://ci.appveyor.com/api/projects/status/pg5qvt62y16bu4k5?svg=true)](https://ci.appveyor.com/project/r-darwish/anyway-sdk-python)
Python SDK for [anyway.co.il](https://anyway.co.il).

## Installation
This package requires Python 3.5 and above. It does not available in PyPi yet, so installation should be performed by checking out the git repository and running:

``` shell
pip install -e .
```

## Example usage

``` python
from anywaysdk import Anyway
anyway = Anyway()
accidents = anyway.get_accidents(location="מגדל משה אביב", distance_in_km=0.2)
for accident in accidents:
    if 'address' in accident:
        print(accident['address'])
```
