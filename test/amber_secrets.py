#
# Routine to fetch Amber credentials to be used during test
#

import boto3
import base64
import json
import sys

def get_secrets(filter=None):

    if filter is not None and type(filter) != list:
        raise ValueError("get_secrets() filter must be a list")

    secret_name = "amber-test-users"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )

    # Decrypts secret using the associated KMS CMK.
    # Depending on whether the secret is a string or binary, one of these fields will be populated.
    if 'SecretString' in get_secret_value_response:
        secrets = get_secret_value_response['SecretString']
    else:
        secrets = base64.b64decode(get_secret_value_response['SecretBinary'])

    # load secret string into dict
    secret_dict = json.loads(secrets)

    # if specified, filter only the secrets we want
    out = {}
    if filter is not None:
        for f in filter:
            if f in secret_dict:
                out[f] = secret_dict[f]
            else:
                out[f] = {}
    else:
        out = secret_dict

    return out

if __name__ == '__main__':
    keys = list(sys.argv[1:])
    s = get_secrets(keys)
    print(json.dumps(s, indent=4))