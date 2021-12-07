from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask,jsonify,redirect, make_response
import cv2
import numpy as np
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import os

from package.saveimg import Save_img
from package.cloudmersive import Cloudmersive
from package.jsonproccessing import Json_proccessing

from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/urlunprocessed",  methods = ['POST'])

def dateJS():
    if request.get_json():

        req = request.get_json()

        print("****"*10)

        url_img = req["url_img_unprocessed"]
        print("url_img_unprocessed:")
        print(url_img)

        #save img
        Save_img.save(url_img)
        img_name = Save_img.save(url_img)[1]
        print("****************")
        # print(img_name)
        print("Processing OCR....")
        #------------------------------------------------------------        

        #consume cloudmersive
        api_key = 'bf31c792-15e4-471c-913c-f9b7473e5f6c'    #Eynher access key 
        json_ocr = Cloudmersive.OCR(api_key, img_name)[0]   

        url_img_processed = {
            'url_img_process': Cloudmersive.OCR(api_key, img_name)[1] 
        }     
            
        

        #json_proccessing
        elec_param_motor = Json_proccessing.json_proccessing(json_ocr)[0]
        gral_param_motor = Json_proccessing.json_proccessing(json_ocr)[1]        

        # print(OCR_result)
        # print("****************")
        # print( elec_param_motor)
        # print("****************")
        # print( gral_param_motor)        
        
        


        
        response = [ url_img_processed, elec_param_motor , gral_param_motor]


        res = make_response(jsonify(response), 200)
        
        return res


    else:
        return "No JSON received", 400


@app.route("/foo")
def index():
    return 'Decimetrix Power Dragon'

if __name__ == '__main__':

  app.run()
#   app.run("0.0.0.0", debug=False)