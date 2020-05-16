# amber-python-sdk

The Boon Amber SDK is a Python 3 project and can be installed via pip. After cloning the `amber-python-sdk` repository to the current directory, run:

```
pip install amber-python-sdk
```

# API credentials

An _api-key_ and _api-tenant_ credential pair must be obtained from Boon Logic to use the Amber SDK. These provide authentication to the Amber server and will be unique to your obtained license.

After importing `boonamber`, you must call `boonamber.set_credentials` to provide the package with your `api_key` and `api_tenant` credential pair:

```
import boonamber as amber

amber.set_credentials(api_key='my-key', api_tenant='my-tenant')
```

# Connectivity test

The following Python script provides a basic proof-of-connectivity:

*connect-example.py*

```
import boonamber as amber
import sys

# set API credentials
amber.set_credentials(api_key='api-key', api_tenant='api-tenant')

# list current sensors in tenant namespace
success, response = amber.sensor_list()
if not success:
    print("could not list sensors: {}".format(response))
    sys.exit(1)
print("sensors: {}".format(response))
```

Running the connect-test.py script should yield something like:
```
$ python connect-example.py
sensors: <list of current sensor-ids in tenant namespace> 
```
