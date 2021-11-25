from package.saveimg import Save_img
from package.cloudmersive import Cloudmersive
from package.jsonproccessing import Json_proccessing


#save img in local storage

# url_img = 'https://bucketpowerdragons3test201211-dev.s3.us-east-2.amazonaws.com/public/Test/PictureTest_3.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLWVhc3QtMiJGMEQCIEP%2FBlW45KZ72Apb%2FVX7gogeiYM7kNw%2BUrYJXR6MBhVHAiA80ZtZlsi7JdGVT%2F2XsNdEfefyKTrx8SdgK%2BiIRry7GiqQBghIEAAaDDAwMTUwODI5NDc0MCIMXYX52hi2BRAldgVbKu0FuowrX65fKantrdns2h2pUTKTLAHVKLazcOVzg0EP1nfAf5h1vmHOl%2Fsdw91I7auvD8aamv%2BPMzUycG%2FOoSJvJLm5PZNHr9%2BVsDnH1KtxttbJ6WSmmaTxO%2BMZOeYxS5UNMDb1LeNNC1LlDKPh2TDKVLAMysqasPqm5FP8fQzkeyJ31E6yLal%2B2ZhxL9mN1s5R5BxX4YRe1WuRrWDxEQPSSRWWwHrLKrlJ98AgKL8BeK0PvgipF6MQuvaY5Tdk%2FtD2D26ozhFOWEGli0k9RISGbTdv5M8LfL2sfplqUSsSnoJozCRwEnAEKRc8K3WCqydsBrNIoCGEfKtxNdLj6jZiV6cZ07TcxRCtrQnVyRkAruwOQs7vgxeCYiL03YQh%2BOlCc8%2FAOnvyYTYfaEj%2BXjFirtr9aN03EzUH5g6DlZf5sXG1a7OmwguWWQe2sJL5%2FkFL672uWYhZNxG6ifYuMsBJjjumZiOyEbOW%2FSVR0cySI%2F7%2FyWl3%2BS4ZGgb%2BidMzr2MrMJYv4gPvuL8P7jJVca8UfFOq0xtxPEd2U2PNfsrzwwJkDiCY%2BQHS9Nz%2BNJMKfIpngYVjJdft7btVV81iFCn9mIP9tqovOgED2wKNTrNX74QcY66oqYIWj5mRDZZTyp7aBiLVF60GIKYWM%2F1sp%2FAtMfB5jdx6TFiz8MsblKDg%2B3gQRtyRnmeBivb%2BCHr702SCoCgIxfEv%2FazSYLVKkJXgcE%2BBH75Yv%2BJa0oJGMuArxBzbCxjwKRpUKOtQsAphWcaPtUSjEsFkwXovPswP9seoA73CQ3tTY5%2FN7demz1dYyfnGajPvU4xu8sKGGmZ0K4QxNr6icWcm1cM9aq%2FOO4tBBVV6TMOwTIpPaIu9va3pkuvRWrcs3TP3xDU%2Fzho9ydayIk%2FMPPFFtGLk37yo2bp1fxeLIsxqn0HH587WiLAH2b2z9olGTsZB%2FyIKicQ4Cem1k1nfclLtxzeZWebze%2Fnpk0IPVh2K8XsMMTgw54swr430jAY6iQJrzZtuf5sWCq%2B%2FffLKqQjurx5yxuyuflQhOuMqr7GAEHf9hgP78slfLg7d52rCuIj6nfpjhoEmYTcBUVoFdnT7AUGWmWrc0ZgD00AI3fR1Qufj6fS5jiuyLBGMaMs6YDt5wO5cEKoxpB3WY0N3wlZPbNNRmqoHgut5Cn%2BySSAKf9nH2uHmUSX%2FZ01G0IEAw%2BJ4DhNazAYvha67rUyT1o96mGOAhF6CfEX2qAdXiCsKWC0KAWryR2tWDkac5w8mzYJ%2BcM1Lule0DAEpfTtV%2B%2FoRU3LwEP53rogCaINtYVXnBA5sKJ%2FGB%2FIWgrQwkE7kfobdFQwM3DYOgAHuxgvwBpJL6QRUMg120nHM&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211123T153538Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604799&X-Amz-Credential=ASIAQAWPGYBKCAVTPXLW%2F20211123%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=958fd636eaff93db685b691b36888b9edbcd070c5fb759efc7219765a04e4b5f'
# url_img = 'https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT35_Photo3.jpg'
# url_img = 'https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT66_Photo1.jpg'
# url_img = 'https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT40_Photo3.jpg'
# url_img = 'https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT46_Photo9.jpg'
# url_img = 'https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT46_Photo9.jpg'
url_img = 'https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/ATT82_Photo1.jpg'

Save_img.save(url_img)
img_name = Save_img.save(url_img)[1]
print("****************")
# print(img_name)
print("Processing OCR....")



#consume cloudmersive
api_key = 'c4e49e4a-7a7e-4a6e-9805-3ef0db25d5f8'    #Paola access key 
json_ocr = Cloudmersive.OCR(api_key, img_name)


#json_proccessing
elec_param_motor = Json_proccessing.json_proccessing(json_ocr)[0]
gral_param_motor = Json_proccessing.json_proccessing(json_ocr)[1]

# print(OCR_result)
# print("****************")
# print( elec_param_motor)
# print("****************")
# print( gral_param_motor)






#enviar a postgreSQL

import psycopg2
from psycopg2 import pool

#enviar a postgreSQL

DB_HOST = "ec2-52-4-100-65.compute-1.amazonaws.com"
DB_NAME = "denang56diacm9"
DB_USER = "uflakclinfsavi"
DB_PASS = "7a88a43c58809174e726e5361184467538cc2ea2b46fb503add7a9b1ca6774d8"

try:
    postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user=DB_USER,
                                                         password=DB_PASS,
                                                         host=DB_HOST,
                                                         port="5432",
                                                         database=DB_NAME)
    if (postgreSQL_pool):
        print("Connection pool created successfully")

    # Use getconn() to Get Connection from connection pool
    ps_connection = postgreSQL_pool.getconn()

    if (ps_connection):
        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor()
        
        #valores a insertar
        insert_elect_param = "INSERT INTO electric_param_motor (hp,voltage,amperage,powerfactor,efficiency,servicefactor,rpm,hz,phases) VALUES ('" +elec_param_motor["HP"]+"','"+elec_param_motor["Voltage"]+"','"+ elec_param_motor["amperage"]+"','"+ elec_param_motor["powerfactor"] +"','"+ elec_param_motor["efficiency"]+"','"+elec_param_motor["servicefactor"]+"','"+elec_param_motor["rpm"]+"','"+ elec_param_motor["HZ"]+"','"+ elec_param_motor["phases"]+"');"
        insert_gral_param = "INSERT INTO gral_param_motor (insulationclass,manufacturer,serialnumber,enclousure,modelnumber,CAT,Weight,DATE,temperature,frame,duty) VALUES ('" +gral_param_motor["insulationclass"] +"','"+gral_param_motor["manufacturer"] +"','"+gral_param_motor["serialnumber"] +"','"+gral_param_motor["enclousure"] +"','"+ gral_param_motor["modelnumber"]+"','"+gral_param_motor["CAT"] +"','"+gral_param_motor["Weight"] +"','"+gral_param_motor["DATE"]+"','"+gral_param_motor["temperature"]+"','"+gral_param_motor["frame"]+"','"+gral_param_motor["duty"]+"');"
        
        

        ps_cursor.execute(insert_elect_param)
        ps_connection.commit()
        ps_cursor.execute(insert_gral_param)
        ps_connection.commit()
        ps_cursor.close()

        # Use this method to release the connection object and send back to connection pool
        postgreSQL_pool.putconn(ps_connection)
        print("Insert value in PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    # use closeall() method to close all the active connection if you want to turn of the application
    if postgreSQL_pool:
        
        postgreSQL_pool.closeall
    print("PostgreSQL connection pool is closed")
