from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask,jsonify,redirect, make_response
import cv2
import numpy as np
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import os



app = Flask(__name__)



@app.route("/dateurl",  methods = ['POST'])

def dateJS():
    if request.get_json():

        req = request.get_json()

        print("****"*10)

        img_n = req["img-number"]
        print("img-number:")
        print(img_n)

        
        print("Welcome to the OCR API By Decimetrix")

        # Configure API key authorization: Apikey
        configuration_ocr = cloudmersive_ocr_api_client.Configuration()
        # configuration_ocr.api_key['Apikey'] = 'c824fa8b-f424-4605-963f-a9a2ad806a39'    #Mi clave de acceso
        configuration_ocr.api_key['Apikey'] = 'bf31c792-15e4-471c-913c-f9b7473e5f6c'    #clave de acceso Gustavo
        
        # create an instance of the API class
        api_instance_ocr = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration_ocr))
        
        #llamado de la API
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
        
          # img = cv2.imread(path)
          img = path
        
          api_response = OCR_cloudmersive(path)
          result = api_response.to_dict()
        #   print(result)
        
          for i in range (len(result['words'])):
            img = boxes_draw(img, result, i)
          cv2.imshow("result", img)
          path = 'C:/Projects/DECIMETRIX/frontend-ocr-app/API-ocr/plates_sample/processed-plates'
          cv2.imwrite(os.path.join(path , 'processed_'+str(img_number)+'.png'), img)
          cv2.imwrite('processed_Photo'+str(img_number)+'.png',img)
          cv2.waitKey()

          return result
        
        
        #Diccionario con los nombres de las imágenes y la ruta de acceso a su localización
        dic = {'img_1' : 'ATT32_Photo5.jpg',
               'img_2' : 'ATT35_Photo3.jpg',
               'img_3' : 'ATT36_Photo4.jpg',
               'img_4' : 'ATT38_Photo1.jpg',
               'img_5' : 'ATT40_Photo3.jpg',
               'img_6' : 'ATT46_Photo9.jpg',
               'img_7' : 'ATT56_Photo2.jpg',
               'img_8' : 'ATT59_Photo5.jpg',
               'img_9' : 'ATT60_Photo1.jpg',
               'img_10' : 'ATT63_Photo4.jpg',
               'img_11' : 'ATT66_Photo1.jpg',
               'img_12' : 'ATT68_Photo3.jpg',
               'img_13' : 'ATT82_Photo1.jpg',
               'img_14' : 'ATT89_Photo3.jpg',
               'img_15' : 'ATT92_Photo2.jpg',
               'img_16' : 'ATT95_Photo3.jpg',
               'img_17' : 'ATT105_Photo2.jpg',
               'img_18' : 'ATT109_Photo4.jpg',
               'img_19' : 'ATT131_Photo3.jpg',
               'img_20' : 'ATT137_Photo3.jpg',
               'img_21' : 'ATT147_Photo3.jpg',
               'img_22' : 'ATT150_Photo3.jpg',
               'img_23' : 'ATT155_Photo2.jpg',
               'img_24' : 'ATT174_Photo2.jpg',
               }
        
        #Change this path to your image folder
        route_access = "C:/Projects/DECIMETRIX/frontend-ocr-app/API-ocr/plates_sample/"
        
        
        #Puesta en marcha del programa
        
        #La variable path es la dirección completa de alojamiento de la imagen
        img_number = img_n
        path = route_access + dic['img_'+str(img_number)]
        
        #Llamado del programa
        # response = OCR_nameplate(path)
        response = OCR_nameplate("https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT35_Photo3.jpg")


        # response = {
        #     "HP_motor": 30,
        #     "V_motor": 30,
        #     "F_motor": 30,
        # }

        print("Image processed successfully")
        print("****"*10)


        res = make_response(jsonify(response), 200)
        
        return res






    else:
        return "No JSON received", 400


@app.route("/foo")
def index():
    return 'python serve'

if __name__ == '__main__':

  app.run()