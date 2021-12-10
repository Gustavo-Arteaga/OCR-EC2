from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import make_response
from src.image_processing import ImageProcessing

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
CORS(app)

@app.route("/urlunprocessed",  methods=['POST'])
def process_ocr():
    if request.get_json():
        try:
            #Recive the URL of the image  
            req = request.get_json()
            url_img = req["url_img_unprocessed"]
            #Execute OCR Image Processig 
            image_processing = ImageProcessing(url_img)
            response = image_processing.run_cm()
            #Generate the Response
            res = make_response(jsonify(response), 200)
            return res
        except:
            return "Processing error", 400
    else:
        return "No json file received", 400

@app.route("/foo")
def index():
    return 'Decimetrix Power Dragon'

if __name__ == '__main__':
    app.run(debug=True)
    #app.run("0.0.0.0", debug=False)
