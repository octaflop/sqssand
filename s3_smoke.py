import os

import boto3
import random
from botocore.exceptions import ClientError

# Testing s3 stuff


S3_BUCKET = 'bucket-of-sand-09f9'

try:
    from credentials import *  # noqa
except ImportError:
    pass


sqs = boto3.client('sqs',
                   aws_access_key_id=AWS_ACCESS_KEY,
                   aws_secret_access_key=AWS_SECRET_KEY)

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY)


def create_bucket():
    region = REGION
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=S3_BUCKET,
                                CreateBucketConfiguration=location)
    except ClientError as e:
        print(e)
        return False
    return True


def upload_files():
    files = os.listdir('./imgs')
    for i, f in enumerate(files):
        rand = random.randint(0, 500)
        s3.upload_file(f'./imgs/{f}', S3_BUCKET, f's3-upload-{i}-{rand}-{f}')


def iterate():
    page_iterator = s3.get_paginator('list_objects').paginate(
        Bucket=S3_BUCKET,
    )

    for page in page_iterator:
        print('Marker', page['Marker'])
        print('Len page', len(page['Contents']))
        import ipdb
        ipdb.set_trace()


# resp = {'ResponseMetadata':
#         {'RequestId': '72DEF15B703E6F66', 'HostId': 'yzqMNg25hoq2RxW9Wql/Sz+grHT8HXl80D1zKKnsPPB+NvwQ+qHaOfvMQmUiL0UK8TcIP3qeiW8=',
#          'HTTPStatusCode': 200,
#          'HTTPHeaders':
#          {'x-amz-id-2': 'yzqMNg25hoq2RxW9Wql/Sz+grHT8HXl80D1zKKnsPPB+NvwQ+qHaOfvMQmUiL0UK8TcIP3qeiW8=',
#           'x-amz-request-id': '72DEF15B703E6F66', 'date': 'Mon, 21 Oct 2019 20:42:28 GMT',
#           'x-amz-bucket-region': 'us-west-2', 'content-type': 'application/xml', 'transfer-encoding': 'chunked',
#           'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'IsTruncated': False,
#         'Marker': '',
#         'Contents': [
#             {'Key': '0MSLvRcU8FOHZA35zW78IZiuUnWVxygQ3CtaLZNjjKQ.jpg-s3-upload-3', 
#             'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 24, tzinfo=tzutc()), 'ETag': '"1d8479535df091be00f25450e59233eb"', 'Size': 276805, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': '0vj25wbxxt3z.png-s3-upload-7', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 25, tzinfo=tzutc()), 'ETag': '"46c70a1d22811cdefc0b65b31046b78b"', 'Size': 1120108, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': '3SMcENH.jpg-s3-upload-16', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 27, tzinfo=tzutc()), 'ETag': '"c0f1617174a7ebde51c63baedfc0f2fa"', 'Size': 492518, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'CBcnNs9.jpg-s3-upload-0', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 24, tzinfo=tzutc()), 'ETag': '"cd2fcc8bc635c5d485e969152edf870c"', 'Size': 198076, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Fleetwood-Mac-Rumours-album-covers-billboard-1000x1000.jpg-s3-upload-15', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 26, tzinfo=tzutc()), 'ETag': '"8e36b6c3b8f02b34080bd87e6aec7e4a"', 'Size': 89920, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Green-Day-American-Idiot-album-covers-billboard-1000x1000.jpg-s3-upload-2', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 24, tzinfo=tzutc()), 'ETag': '"51a8dda9ec8de8842c5d8bf4934e9f55"', 'Size': 86705, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Janet-Jackson-Rhythm-Nation-1814-album-covers-billboard-1000x1000.jpg-s3-upload-8', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 25, tzinfo=tzutc()), 'ETag': '"9d4b77a7c9807522e5f5c0e241d57084"', 'Size': 66245, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Lady-Gaga-Fame-Monster-album-covers-billboard-1000x1000.jpg-s3-upload-1', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 24, tzinfo=tzutc()), 'ETag': '"cc0f4e862696b2fd51368a06e9dbd4e4"', 'Size': 103839, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Ohio-Players-Honey-album-covers-billboard-1000x1000.jpg-s3-upload-9', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 25, tzinfo=tzutc()), 'ETag': '"b5d59f07ff6c39c030cb1b2e1bab94b1"', 'Size': 151611, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Taylor-Swift-1989-album-covers-billboard-1000x1000.jpg-s3-upload-6', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 25, tzinfo=tzutc()), 'ETag': '"7dbb8cda1ba30ce714cbd86278b37b42"', 'Size': 82144, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Wanted-The-Outlaws-Waylon-Jennings-Jessi-Colter-Willie-Nelson-Tompall-Glaser-album-covers-billboard-1000x1000.jpg-s3-upload-4', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 25, tzinfo=tzutc()), 'ETag': '"3da99a858aee763bbbfa2dde5ab75d40"', 'Size': 216056, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'Yeah-Yeah-Yeahs-Its-Blitz-album-covers-billboard-1000x1000.jpg-s3-upload-11', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 26, tzinfo=tzutc()), 'ETag': '"ed4fc3158111f6331ccbf92daa68b5f5"', 'Size': 90543, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'cjRLHPZx7hDWL6SWkeFlUVxEAeBChT9dr-Rq9bZ7J_A.jpg-s3-upload-14', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 26, tzinfo=tzutc()), 'ETag': '"10ad4de20c055474dcebff10ba4cbab8"', 'Size': 82857, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'goBR5_AJv6fvvr0RCbprOHsr4E3MJd9mlFddalEZUPM.jpg-s3-upload-13', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 26, tzinfo=tzutc()), 'ETag': '"074882971c67cebc7fe6dd6a39ec6a41"', 'Size': 172465, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'mFxz7m7vF7XQC09qqJg2mRCNT7g9wzidAVCuw4agQe4.jpg-s3-upload-5', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 25, tzinfo=tzutc()), 'ETag': '"19fffbd249931dbc2452b8069d567510"', 'Size': 205132, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 'qphkgomLaz-MZPGJ0po_zUYpGauM13RYJVc8ojNYvU4.jpg-s3-upload-10', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 26, tzinfo=tzutc()), 'ETag': '"89897c13d5a9e1d7fdcedafbc0c45dfa"', 'Size': 390587, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}, {'Key': 't537_9XqUBloqntzCYGjJmY7fIH1Uz-6HLe0y27B0gk.jpg-s3-upload-12', 'LastModified': datetime.datetime(2019, 10, 21, 20, 40, 26, tzinfo=tzutc()), 'ETag': '"4f446caba67adcd495474e60a1cca2e9"', 'Size': 85276, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'faris', 'ID': 'f6be03a2aadffe0cf3fbf26db1f9350a370fc47c2e12953ef0814ed6666df84c'}}], 'Name': 'bucket-of-sand-09f9', 'Prefix': '', 'MaxKeys': 1000, 'EncodingType': 'url'}
