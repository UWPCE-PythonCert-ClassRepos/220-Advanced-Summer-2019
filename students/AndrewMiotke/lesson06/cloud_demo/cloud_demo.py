import requests
from pprint import pprint
import boto3
from botocore.exceptions import ClientError

# Initial configuration for AWS S3
region = 'us-west-2'
s3 = boto3.client('s3', region_name=region)


file_url = 'http://data.teleona.com/iris.csv'
r = requests.get(file_url, allow_redirects=True)

with open(file_url.split('/')[-1], 'wb') as file:
    file.write(r.content)


# Create an S3 bucket programmatically
# Bucket already created so I'm commenting out this code
# Change the bucket_name variable to create a new bucket and run the try
bucket_name ='andrew.miotke.demo.bucket'
# try:
#     location = {'LocationConstraint': region}
#     s3.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration=location,
#     )
# except ClientError as ce:
#     print(ce)


# List buckets
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket)


# Upload data to bucket
# try:
#     response = s3.upload_file(
#         'iris.csv',
#         bucket_name,
#         'iris_data.csv'
#     )
# except ClientError as ce:
#     print(ce)


# List objects in a bucket
response = s3.list_objects(Bucket=bucket_name)
for obj in response['Contents']:
    print(f'{obj}\n')
