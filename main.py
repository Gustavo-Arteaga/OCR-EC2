from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask,jsonify,redirect, make_response
import cv2
import numpy as np
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import os

from package.saveimg import Save_img
from package.cloudmersive import Cloudmersive
from package.jsonproccessing import Json_proccessing



app = Flask(__name__)



@app.route("/dateurl",  methods = ['POST'])

def dateJS():
    if request.get_json():

        req = request.get_json()

        print("****"*10)

        url_img = req["img_url"]
        print("img_urlr:")
        print(url_img)

        #save img
        Save_img.save(url_img)
        img_name = Save_img.save(url_img)[1]
        print("****************")
        # print(img_name)
        print("Processing OCR....")
        #------------------------------------------------------------        

        #consume cloudmersive
        api_key = 'c4e49e4a-7a7e-4a6e-9805-3ef0db25d5f8'    #Paola access key 
        json_ocr = Cloudmersive.OCR(api_key, img_name)[0]        
        url_img_processed = Cloudmersive.OCR(api_key, img_name)[1]        
        

        #json_proccessing
        elec_param_motor = Json_proccessing.json_proccessing(json_ocr)[0]
        gral_param_motor = Json_proccessing.json_proccessing(json_ocr)[1]        

        # print(OCR_result)
        # print("****************")
        # print( elec_param_motor)
        # print("****************")
        # print( gral_param_motor)        
        
        
        
        
        

        # #enviar a postgreSQL        

        # import psycopg2
        # from psycopg2 import pool        

        # #enviar a postgreSQL        

        # DB_HOST = "ec2-52-4-100-65.compute-1.amazonaws.com"
        # DB_NAME = "denang56diacm9"
        # DB_USER = "uflakclinfsavi"
        # DB_PASS = "7a88a43c58809174e726e5361184467538cc2ea2b46fb503add7a9b1ca6774d8"        

        # try:
        #     postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user=DB_USER,
        #                                                          password=DB_PASS,
        #                                                          host=DB_HOST,
        #                                                          port="5432",
        #                                                          database=DB_NAME)
        #     if (postgreSQL_pool):
        #         print("Connection pool created successfully")        

        #     # Use getconn() to Get Connection from connection pool
        #     ps_connection = postgreSQL_pool.getconn()        

        #     if (ps_connection):
        #         print("successfully recived connection from connection pool ")
        #         ps_cursor = ps_connection.cursor()
                
        #         #valores a insertar
        #         insert_elect_param = "INSERT INTO electric_param_motor (hp,voltage,amperage,powerfactor,efficiency,servicefactor,rpm,hz,phases) VALUES ('" +elec_param_motor["HP"]+"','"+elec_param_motor["Voltage"]+"','"+ elec_param_motor["amperage"]+"','"+ elec_param_motor["powerfactor"] +"','"+ elec_param_motor["efficiency"]+"','"+elec_param_motor["servicefactor"]+"','"+elec_param_motor["rpm"]+"','"+ elec_param_motor["HZ"]+"','"+ elec_param_motor["phases"]+"');"
        #         insert_gral_param = "INSERT INTO gral_param_motor (insulationclass,manufacturer,serialnumber,enclousure,modelnumber,CAT,Weight,DATE,temperature,frame,duty) VALUES ('" +gral_param_motor["insulationclass"] +"','"+gral_param_motor["manufacturer"] +"','"+gral_param_motor["serialnumber"] +"','"+gral_param_motor["enclousure"] +"','"+ gral_param_motor["modelnumber"]+"','"+gral_param_motor["CAT"] +"','"+gral_param_motor["Weight"] +"','"+gral_param_motor["DATE"]+"','"+gral_param_motor["temperature"]+"','"+gral_param_motor["frame"]+"','"+gral_param_motor["duty"]+"');"
                
                        

        #         ps_cursor.execute(insert_elect_param)
        #         ps_connection.commit()
        #         ps_cursor.execute(insert_gral_param)
        #         ps_connection.commit()
        #         ps_cursor.close()        

        #         # Use this method to release the connection object and send back to connection pool
        #         postgreSQL_pool.putconn(ps_connection)
        #         print("Insert value in PostgreSQL connection")        

        # except (Exception, psycopg2.DatabaseError) as error:
        #     print("Error while connecting to PostgreSQL", error)        

        # finally:
        #     # closing database connection.
        #     # use closeall() method to close all the active connection if you want to turn of the application
        #     if postgreSQL_pool:
                
        #         postgreSQL_pool.closeall
        #     print("PostgreSQL connection pool is closed")        



        
        response = [elec_param_motor , gral_param_motor, url_img_processed]


        res = make_response(jsonify(response), 200)
        
        return res






    else:
        return "No JSON received", 400


@app.route("/foo")
def index():
    return 'python serve'

if __name__ == '__main__':

  app.run()