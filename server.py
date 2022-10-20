# import main Flask class and request object
from unicodedata import category
from flask import Flask, request
from flask_cors import CORS
from emissions_calculator.usableModel import predict
from emissions_calculator.vocab import text_pipeline
import CategoryMapping
import json
import requests
import os
from dotenv import load_dotenv

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
        # check that the product cat was able to be scraped
        print(product["Category"] in list(CategoryMapping.AMAZON_TO_API_CATEGORY.keys()))
        if product["Category"] != "" and product["Category"] in list(CategoryMapping.AMAZON_TO_API_CATEGORY.keys()):
            category = product["Category"]
        #if not guess using AI
        else:
            category = predict(product["productTitle"], text_pipeline)
        print(category)
        API_cat = CategoryMapping.AMAZON_TO_API_CATEGORY[category]
        print(API_cat)
        load_dotenv()
        MY_API_KEY = os.getenv('MY_API_KEY')
        URL = 'https://beta3.api.climatiq.io/estimate'
        headers = {
        'Authorization': 'Bearer {KEY}'.format(KEY = MY_API_KEY),
        'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            "emission_factor": { 
                "id": CategoryMapping.API_CATEGORY_TO_ACTIVITY_ID[API_cat],
                "region": "us"
            },
            "parameters": {
                "money": product["productCost"],
                "money_unit": "usd"

            }
        }
        print(data)
        response = requests.post(URL, headers=headers, json=data).json()
        return json.dumps({"emissions": response})
    else:
        return 'Content-Type not supported!'



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)