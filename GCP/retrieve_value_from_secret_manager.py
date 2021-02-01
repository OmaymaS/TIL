from google.cloud import secretmanager

## define parameters
PROJECT_ID = "project_x"
SECRET_NAME = "APP_KEY"
SECRET_VERSION = "1" # "latest" to get the latest version

# compose secret_id out of variables
secret_id = f'projects/{PROJECT_ID}/secrets/{SECRET_NAME}/versions/{SECRET_VERSION}'

## retrieve value
secret_value = client.access_secret_version(request={"name": secret_id}).payload.data.decode("utf-8")