- Set/change project.

`gcloud config set project {PROJECT}`

- Build image and submit to GCR.
`gcloud builds submit --tag gcr.io/`

-  Deploy a gcr image on cloudrun.
`gcloud run deploy --image gcr.io/{PROJECT}/{NAME}`