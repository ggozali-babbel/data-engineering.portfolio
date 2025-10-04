import boto3
from datetime import datetime

def s3_file_upload(FILE_NAME, BUCKET_NAME):

    # Extract year and month from today's date
    current_date = datetime.now()
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')

    # Build the S3 key: year/month/filename
    s3_key = f"{year}/{month}/{FILE_NAME}"

    # Initialize S3 client (credentials must be set up)
    s3 = boto3.client('s3')

    # file upload to s3 bucket
    s3.upload_file(FILE_NAME, BUCKET_NAME, s3_key)

    print(f"Uploaded {FILE_NAME} to s3://{BUCKET_NAME}/{s3_key}")