## Example of service account impersonation to use automl API

import google.auth.impersonated_credentials
from google.oauth2 import service_account
from google.cloud import automl

## select the scope from https://cloud.google.com/sdk/gcloud/reference/beta/compute/instances/set-scopes
## here we want to use automl, so we select the following:
TARGET_SCOPES = "https://www.googleapis.com/auth/cloud-platform" 

## replace with your values ----------------
SERVICE_ACCOUNT_CREDENTIALS_PATH = 'cred.json'
SERVICE_ACCOUNT = "serviceaccount_name@project_id.iam.gserviceaccount.com"
PROJECT_ID = "dddddddd"
MODEL_ID = "xxxxxxxxxxx" 
FILE_PATH = "image.jpeg"
## ------------------------------------------

## set source credentials
source_credentials = (
    service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_CREDENTIALS_PATH , ## path to service account credentials json file
        scopes=TARGET_SCOPES)
    )
## use the source credentials to acquire credentials to impersonate another service account
target_credentials = google.auth.impersonated_credentials.Credentials(
    source_credentials=source_credentials,
    target_principal=SERVICE_ACCOUNT, 
    target_scopes=TARGET_SCOPES,
    )
## create client using the target credentials
prediction_client = automl.PredictionServiceClient(credentials=target_credentials)

# get the full path of the model
model_full_id = automl.AutoMlClient.model_path(
    PROJECT_ID, "us-central1", MODEL_ID
)

# read the image file
with open(FILE_PATH, "rb") as content_file:
    content = content_file.read()
image = automl.Image(image_bytes=content)
payload = automl.ExamplePayload(image=image)

## set parameters
params = {"score_threshold": "0.5"}

## send predcit request
request = automl.PredictRequest(
    name=model_full_id,
    payload=payload,
    params=params
)
response = prediction_client.predict(request=request)
