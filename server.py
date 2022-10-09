# import main Flask class and request object
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def start():
    return "server running"

@app.route('/get_emissions', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request
        
        return json
    else:
        return 'Content-Type not supported!'



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)