# The Python SWC Registry Library


[![CircleCI](https://circleci.com/gh/SmartContractSecurity/SWC-registry-python.svg?style=svg)](https://circleci.com/gh/SmartContractSecurity/SWC-registry-python)	

## Description
Python library for accessing SWC-registry content.

## Installation

```console
$ pip install -U swc-registry
```

## Example
```python
from swc_registry import SWC

swc = SWC('SWC-100')
print(swc.title)

// Function Default Visibility
```


## Behaviour

On first use of the SWC methods, the SWC registry is initialized from file (swc-definition.json) out cache. If user wants to get the latest information about SWC-registry he needs to pass the second argument of SWC class.

### Get latest version
```python
from swc_registry import SWC

swc = SWC('SWC-100', True)
print(swc.title)

// Function Default Visibility
```
## Contribution