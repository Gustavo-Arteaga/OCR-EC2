import os
import cv2
import boto3
import numpy as np
from config import Config
from package.cloudmersive import Cloudmersive
from package.jsonproccessing import JsonProccessing

AWS_ACCESS_KEY_ID = Config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = Config.AWS_SECRET_ACCESS_KEY
API_KEY = Config.API_KEY

class ImageProcessing:
    def __init__(self, img_link):
        #Save image link
        self.img_link = img_link
        print(img_link)
        #Find the image name in te link 
        for i in range(len(img_link)-1, 0, -1):
            if img_link[i] == '/':
                img_name = img_link[i+1:]
                break
        #Save image name
        self.img_name = img_name
        #Find bucket name name in te link
        for i in range(len(img_link)-1):
            if img_link[i] == '.':
                bucket_name = img_link[8:i]
                break
        #Save bucket name
        self.bucket_name = bucket_name

    def download_file(self):     
        #Create de Output Path
        image_path = os.path.join('./resource/unprocessed/', self.img_name)
        #Create AWS S3 Client and Download the File
        s3=boto3.client('s3', aws_access_key_id = AWS_ACCESS_KEY_ID , aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        s3.download_file(self.bucket_name, self.img_name, image_path)
        return image_path

    def upload_file(self, path_upload):
        # Upload img processed to S3 bucket
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        bucket_name = 'img-processed'
        region = 'us-east-2'
        s3.upload_file(path_upload, bucket_name, self.img_name, ExtraArgs={'ACL': 'public-read'})
        url_img_processed = {'url_img_process':"https://"+bucket_name+".s3."+region+".amazonaws.com/"+self.img_name}
        print("OCR Image Uploaded to S3 Bucket...................................")
        return url_img_processed

    def delete_files(self, image_path, ocr_path):
        os.remove(image_path)
        os.remove(ocr_path)
        
    def run_cm(self):
        print('ORC Processing Init.............................................')
        #Download and save AWS Image
        image_path = self.download_file()
        print('Image downloaded '+image_path)
        #Execute Cloudmersive OCR
        print('Executing ORC...................................................')
        ocr_processing = Cloudmersive(API_KEY, self.img_name, image_path)
        processing_result = ocr_processing.OCR()
        json_ocr = processing_result[0]
        ocr_path = processing_result[1]
        #Upload Processed Img to S3
        print('Saving ORC Image in S3..........................................')
        url_img_processed = self.upload_file(ocr_path)
        #Analysis of the JSON file
        print('Analyzing OCR json File.........................................')
        json_processing = JsonProccessing()
        gral_param_motor, elec_param_motor = json_processing.run(json_ocr)
        #Generate the JSON Response
        print('Generating Response.............................................')
        response = [url_img_processed, elec_param_motor, gral_param_motor]
        print('Deleting Temporal Files.........................................')
        #Delete Temporal Files
        self.delete_files(image_path,ocr_path)
        print('ORC Processing Done.............................................')
        return response

    def run_tf(self):
        pass
