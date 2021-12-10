import os
import cv2
import numpy as np
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException

class Cloudmersive:
    def __init__(self, key, img_name, image_path):
        self.key = key
        self.img_name = img_name
        self.image_path = image_path
    #Main Function
    def OCR(self):
        # Configure API key authorization: Apikey
        configuration_ocr = cloudmersive_ocr_api_client.Configuration()
        configuration_ocr.api_key['Apikey'] = self.key  # Access key
        # create an instance of the API class
        self.api_instance_ocr = cloudmersive_ocr_api_client.ImageOcrApi(
            cloudmersive_ocr_api_client.ApiClient(configuration_ocr))
        return self.OCR_nameplate(self.image_path)

    #API Request
    def OCR_cloudmersive(self, image_file, language='ENG', preprocessing='Auto'):
        try:
            # Convert a scanned image into words with location
            api_response = self.api_instance_ocr.image_ocr_image_words_with_location(
                image_file, language=language, preprocessing=preprocessing)
            return api_response
        except ApiException as e:
            print(
                "Exception when calling ImageOcrApi->image_ocr_image_words_with_location: %s\n" % e)

    #Select the Worlds in the Image
    def boxes_draw(self, img, dictionary, index):
        x_ini = dictionary['words'][index]['x_left']
        y_ini = dictionary['words'][index]['y_top']
        width = dictionary['words'][index]['width']
        height = dictionary['words'][index]['height']
        text = dictionary['words'][index]['word_text']
        rectangle = cv2.rectangle(img, (x_ini, y_ini), (x_ini+width, y_ini+height), (255, 0, 0), 2)
        # create same size image of background color
        bg_color = (255, 0, 0)
        bg = np.full((img.shape), bg_color, dtype=np.uint8)
        # draw text on bg
        text_color = (255, 255, 255)
        cv2.putText(bg, text, (x_ini, y_ini-3),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, text_color, 1)
        # get bounding box
        # use channel corresponding to color so that text is white on black background
        x, y, w, h = cv2.boundingRect(bg[:, :, 2])
        # copy bounding box region from bg to img
        result = rectangle.copy()
        result[y-2:y+h+4, x-2:x+w+4] = bg[y-2:y+h+4, x-2:x+w+4]
        return result

    # Call the Functions and Visualitation of OCR
    def OCR_nameplate(self, path):
        img = cv2.imread(path)
        api_response = self.OCR_cloudmersive(path)
        result = api_response.to_dict()
        for i in range(len(result['words'])):
            img = self.boxes_draw(img, result, i)
        #Save OCR Image Result  
        path_upload = os.path.join('./resource/processed/', self.img_name)
        cv2.imwrite(path_upload, img)
        print("Processed Img Generated..................................")        
        return result, path_upload 
