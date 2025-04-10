from google.cloud import aiplatform
import os

aiplatform.init(project="your-gcp-project", location="us-central1")

# Assumes model already deployed to endpoint
ENDPOINT_ID = "your-endpoint-id"

def send_to_vertex(instance: dict):
    endpoint = aiplatform.Endpoint(endpoint_name=ENDPOINT_ID)
    prediction = endpoint.predict(instances=[instance])
    return prediction.predictions[0] if prediction.predictions else None
