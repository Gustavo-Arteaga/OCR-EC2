import numpy as np
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import os
import cv2
class Cloudmersive:
  def __init__(self,key,img_name):
    self.key = key
    self.img_name = img_name

  def OCR(key, img_name):
      # Configure API key authorization: Apikey
      configuration_ocr = cloudmersive_ocr_api_client.Configuration()
      # configuration_ocr.api_key['Apikey'] = 'c824fa8b-f424-4605-963f-a9a2ad806a39'    #My access key
      # configuration_ocr.api_key['Apikey'] = 'bf31c792-15e4-471c-913c-f9b7473e5f6c'    #Gustavo access key 
      configuration_ocr.api_key['Apikey'] = key    #Gustavo access key 
      
      # create an instance of the API class
      api_instance_ocr = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration_ocr))
      
      #Consume API
      def OCR_cloudmersive(image_file, 
                language = 'ENG',
                preprocessing = 'Auto'
                ):
          try:
              # Convert a scanned image into words with location
              api_response = api_instance_ocr.image_ocr_image_words_with_location(image_file, language=language, preprocessing=preprocessing)
              return api_response
          except ApiException as e:
              print("Exception when calling ImageOcrApi->image_ocr_image_words_with_location: %s\n" % e)
      
      #Marcacion de palabras de la placa
      def boxes_draw(img, dictionary, index):
        x_ini = dictionary['words'][index]['x_left']
        y_ini = dictionary['words'][index]['y_top']
        width = dictionary['words'][index]['width']
        height = dictionary['words'][index]['height']
        text = dictionary['words'][index]['word_text']
        rectangle = cv2.rectangle(img,(x_ini,y_ini),(x_ini+width,y_ini+height),(255,0,0),2)
        
        # create same size image of background color
        bg_color = (255,0,0)
        bg = np.full((img.shape), bg_color, dtype=np.uint8)
        
        # draw text on bg
        text_color = (255,255,255)
        cv2.putText(bg, text, (x_ini,y_ini-3), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, text_color, 1)
        
        # get bounding box
        # use channel corresponding to color so that text is white on black background
        x,y,w,h = cv2.boundingRect(bg[:,:,2])
        
        # copy bounding box region from bg to img
        result = rectangle.copy()
        result[y-2:y+h+4, x-2:x+w+4] = bg[y-2:y+h+4, x-2:x+w+4]
        
        return result
      
      
      #Llamada de las funciones y vizualización del OCR
      
      def OCR_nameplate(path):
      
        img = cv2.imread(path)
        api_response = OCR_cloudmersive(path)
        result = api_response.to_dict()
        # print(result)
      
        for i in range (len(result['words'])):
          img = boxes_draw(img, result, i)

          #Upload img processed to S3 bucket
 
        cv2.imwrite('resource/processed/'+img_name,img)
        import boto3
        AWS_ACCESS_KEY_ID = 'AKIAQAWPGYBKHGHVCHH3'
        AWS_SECRET_ACCESS_KEY = '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'
        
        client_s3 = boto3.client('s3', aws_access_key_id= AWS_ACCESS_KEY_ID , aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
        path = 'resource/unprocessed/'+img_name
        bucket_name = 'img-processed'
        region = 'us-east-2'
        client_s3.upload_file(path, bucket_name,img_name, ExtraArgs={'ACL':'public-read'})
        url_img_processed = "https://"+bucket_name+".s3."+region+".amazonaws.com/"+img_name
      #   cv2.waitKey()
        return result, url_img_processed
      
      
      #url de la imagen
      
      
      # path = "https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT35_Photo3.jpg"
      # path = "ATT82_Photo1.jpg"
      # path = "ATT46_Photo9.jpg"
      
      # path = 'src/'+img_name
      path = 'resource/unprocessed/'+img_name 
      
      
      
      #Llamado del programa
      # response = OCR_nameplate(path)
      return OCR_nameplate(path)



