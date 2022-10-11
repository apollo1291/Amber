# import main Flask class and request object
from unicodedata import category
from flask import Flask, request
from flask_cors import CORS
from emissions_calculator.usableModel import predict
from emissions_calculator.vocab import text_pipeline
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def start():
    return "server running"

@app.route('/get_emissions', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product = request.get_json()
        print(product)
        print(product["productTitle"])
        category = predict(product["productTitle"], text_pipeline)
        print(category)
        return json.dumps({"productCategory": category})
    else:
        return 'Content-Type not supported!'



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)