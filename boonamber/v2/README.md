![Logo](../../docs/BoonLogic.png?raw=true)

# Boon Amber Python SDK v2

An SDK for Boon Amber sensor analytics

- __Website__: [boonlogic.com](https://boonlogic.com)
- __Documentation__: [Boon Docs Main Page](https://docs.boonlogic.com)
- __SDK Functional Breakdown__: [amber-python-sdk classes and methods]({{ site.baseurl}}/docs/boonamber/index.html)

## Installation

The Boon Amber SDK is a Python 3 project and can be installed via pip.

```
pip install boonamber
```

## Credentials setup

Note: An account in the Boon Amber cloud must be obtained from Boon Logic to use the Amber SDK.

The license key and secret key should be placed in a file named _~/.Amber.license_ whose contents are the following:

```json
{
    "default": {
        "license-key": "AMBER-ACCOUNT-LICENSE",
        "secret-key": "AMBER-ACCOUNT-SECRET",
        "server": "https://v2.amber.boonlogic.com"
    }
}
```

The _~/.Amber.license_ file will be consulted by the Amber SDK to find and authenticate your account credentials with the Amber server.  Profile configurations may also
be set through a set of environment variables or kwargs when the AmberV2Client object is created.

## Connectivity test

The following Python script provides a basic proof-of-connectivity:

[connect-example.py](../../examples/v2/connect-example.py)

```python
import sys
import json
from boonamber import AmberV2Client, ApiException

try:
    # Use ~/.Amber.license file and "default" profile
    amber = AmberV2Client()
    version_info = amber.get_version()
except ApiException as e:
    print(f"Error: {e}")
    sys.exit(1)

print(json.dumps(version_info.to_dict(), indent=4))
```

Running the connect-example.py script should yield output like the following:
```
$ python connect-example.py
{
    "release": "0.0.405",
    "api-version": "/v2",
    "builder": "ec74f421",
    "expert-api": "dee23681",
    "expert-common": "300a588e",
    "nano-secure": "61c431e2",
    "swagger-ui": "914af396"
}
```
where the dictionary `{}` lists all sensors that currently exist under the given Boon Amber account.

## Full Example

Example to demonstrate each API call

[full-example-v2.py](../../examples/v2/full-example.py)

## Fusion Example

Example to demonstrate submitting data via the label for individual features of a fusion vector.

[fusion-example-v2.py](../../examples/v2/fusion-example.py)

## Advanced CSV file processor

Example of streaming a .csv file.  Full Amber analytic results will be displayed after each streaming request.  

[stream-advanced-v2.py](../../examples/v2/stream-advanced.py)<br>
[output_current.csv](../../examples/v2/output_current.csv)


## Pretrain example

Example of pretraining a .csv file

[pretrain-example-v2.py](../../examples/v2/pretrain-example.py)<br>
[output_current.csv](../../examples/v2/output_current.csv)
