from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import make_response
from werkzeug.exceptions import HTTPException
from src.image_processing import ImageProcessing


def create_app():
    app = Flask(__name__)
    return app


app = create_app()
CORS(app)


@app.errorhandler(400)
def bad_request(e):
    return "Bad Request", 400


@app.errorhandler(404)
def page_not_found(e):
    return "URL not found", 404


@app.errorhandler(Exception)
def internal_server_error(e):
    if isinstance(e, HTTPException):
        return "Internal Server Error", 500
    return "Internal Server Error", 500


@app.route("/urlunprocessed",  methods=['POST'])
def process_ocr():
    try:
        # Recive the URL of the image
        req = request.get_json()
        url_img = req["url_img_unprocessed"]
        # Execute OCR Image Processig
        image_processing = ImageProcessing(url_img)
        response = image_processing.run_cm()
        # Generate the Response 
        res = make_response(jsonify(response), 201)
        return res
    except:
        abort(500)

@app.route("/sendkey",  methods=['POST'])
def image_key_handler():
    try:
        # Recive the URL of the image
        req = request.get_json()
        img_key = req["img_key"]
        # Execute image key processing function
        image_processing = ImageProcessing(img_key)
        response = image_processing.img_key_processing()
        # Generate the Response
        res = make_response(jsonify(response), 201)
        return res
    except:
        abort(500)


@app.route("/foo")
def index():
    return 'Decimetrix Power Dragon'


if __name__ == '__main__':
    app.run(debug=True)
    #app.run("0.0.0.0", debug=False)
