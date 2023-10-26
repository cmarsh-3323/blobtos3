## Blob to S3

Takes a csv file from an azure storage container and uploads to an S3 (Simple Storage Service) bucket using the imports boto3 and BlobServiceClient.

## Installation

Install the required Python packages using the terminal as followed:

`pip install boto3 azure-storage-blob`

## Environment Variables

Before running the script, make sure to set the following environment variables to hide your credentials:

- `azure_account_key`: Azure account key for authentication.
- `aws_access_key`: AWS access key for authentication.
- `aws_secret_key`: AWS secret key for authentication.

## Usage

After setting the required environment variables, run this script in the terminal:

`python your_script.py`

## References

[boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

[BlobServiceClient](https://learn.microsoft.com/en-us/dotnet/api/azure.storage.blobs.blobserviceclient?view=azure-dotnet)


