from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

API_KEY = 'ff5c010010f14afabee6b91f95c35c35'
ENDPOINT = 'https://textanly-python.cognitiveservices.azure.com/'

def client():
    # Authenticate the client
    client = TextAnalyticsClient(
        endpoint=ENDPOINT, 
        credential=AzureKeyCredential(API_KEY))
    return client
