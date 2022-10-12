# import main Flask class and request object
from unicodedata import category
from flask import Flask, request
from flask_cors import CORS
from emissions_calculator.usableModel import predict
from emissions_calculator.vocab import text_pipeline
import CategoryMapping
import json
import requests

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
    
        category = predict(product["productTitle"], text_pipeline)
        API_cat = CategoryMapping.AMAZON_TO_API_CATEGORY[category]

        URL = 'https://beta3.api.climatiq.io/estimate'
        headers = {
        'Authorization': 'Bearer {MY_API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            "emission_factor": { 
                "id": CategoryMapping.API_CATEGORY_TO_EMISSION_FACTOR_ID[API_cat],
                "region": "us"
            },
            "parameters": {
                "money": product["productCost"],
                "money_unit": "usd"

            }
        }
        response = requests.post(URL, headers=headers, data=data)
        return json.dumps({"emissions": response.json()})
    else:
        return 'Content-Type not supported!'



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)