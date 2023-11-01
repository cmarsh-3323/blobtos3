import boto3
import os
from azure.storage.blob import BlobServiceClient

# Blob Storage and AWS S3 credentials
azure_account_name = 'xxxxxxxxx'
azure_account_key = os.environ.get("azure_account_key")
container_name = 'xxxxxxxx'
blob_name = 'xxxxxxx.csv'
aws_access_key = os.environ.get("aws_access_key")
aws_secret_key = os.environ.get("aws_secret_key")
aws_bucket_name = 'xxxxxxxx'

# Start Azure Blob Service Client
azure_blob_service_client = BlobServiceClient(
    account_url=f"https://{azure_account_name}.blob.core.windows.net",
    credential=azure_account_key
)

# Get the blob
blob_client = azure_blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob to a temp file
with open(blob_name, "wb") as my_blob:
    my_blob.write(blob_client.download_blob().readall())

# Start the AWS S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

try:
    # Upload the blob to my AWS S3 bucket
    s3.upload_file(blob_name, aws_bucket_name, blob_name)
    print(f'File "{blob_name}" uploaded successfully to S3.')
except Exception as e:
    print(f'Error occurred while uploading the file to S3: {e}')

