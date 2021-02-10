import boto3
import json

## define parameters (replace by yours)
SECRET_NAME = "secret_name" 
REGION_NAME = "eu-west-1"
PROFILE_NAME = None ## replace with the profile name if you are not using the default

## retrieve credentials from secret manager
session = boto3.session.Session(profile_name = PROFILE_NAME) 
client = session.client(service_name='secretsmanager',region_name=REGION_NAME)
secret_value_response = client.get_secret_value(SecretId=SECRET_NAME)
secret_value_dict = json.loads(secret_value_response['SecretString'])