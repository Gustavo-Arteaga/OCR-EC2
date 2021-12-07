# import tinys3
# S3_ACCESS_KEY = 'AKIAQAWPGYBKHGHVCHH3'
# S3_SECRET_KEY = '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'

# conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,endpoint='s3-eu-west-1.amazonaws.com')

# f = open('resource/processed/ATT40_Photo3.jpg','rb')

# BUCKET = 'bucket-power-dragon-test'
# conn.upload('testpython.png',f,BUCKET)



# import boto
# import boto.s3
# import sys
# from boto.s3.key import Key

# AWS_ACCESS_KEY_ID = 'AKIAQAWPGYBKHGHVCHH3'
# AWS_SECRET_ACCESS_KEY = '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'

# bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
# conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
#         AWS_SECRET_ACCESS_KEY)


# bucket = 'bucket-power-dragon-test'

# testfile = "resource/processed/ATT40_Photo3.jpg"


# def percent_cb(complete, total):
#     sys.stdout.write('.')
#     sys.stdout.flush()


# k = Key(bucket)
# k.key = 'my test file'
# k.set_contents_from_filename(testfile,
#     cb=percent_cb, num_cb=10)


# import boto3
# AWS_ACCESS_KEY_ID =  'AKIAQAWPGYBKHGHVCHH3'
# AWS_SECRET_ACCESS_KEY = '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'

client_s3 = boto3.client('s3', aws_access_key_id= AWS_ACCESS_KEY_ID , aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
file_name = 'ATT40_Photo3.jpg'
path = 'resource/unprocessed/'+file_name
bucket_name = 'img-processed'
region = 'us-east-2'
client_s3.upload_file(path, bucket_name,file_name, ExtraArgs={'ACL':'public-read'})
url_img_processed = "https://"+bucket_name+".s3."+region+".amazonaws.com/"+file_name

print(url_img_processed)

# def upload_files(filename, path):
#     AWS_ACCESS_KEY_ID = 'AKIAQAWPGYBKHGHVCHH3'
#     AWS_SECRET_ACCESS_KEY = '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'
    
#     bucket_name = 'img-processed'
#     s3=boto3.client('s3', aws_access_key_id= AWS_ACCESS_KEY_ID , aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
#     s3.upload_file(path,bucket_name,filename, ExtraArgs={'ACL':'public-read'})
#     img_url_processed = 'https://bucket-power-dragon-test.s3.amazonaws.com/'+filename
#     return img_url_processed

# filename = 'ATT217-Photo3.jpg'
# path = 'resource/unprocessed/'+filename

# upload_files(filename, path)

# print(upload_files(filename, path))