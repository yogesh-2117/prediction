from flask import Flask, render_template
from flask import request, make_response

from flask_cors import CORS
import os
import os.path
import json
from preprocess import prediction

app = Flask(__name__, static_url_path = "", static_folder = "staticFiles")
CORS(app)


obj = prediction()

@app.route("/")
def first_page():
    return render_template("index.html")
    
@app.route('/predict', methods=['POST'])
def predict():
     data = request.get_json()
     print(data)
     val = obj.predictResult(data)
     r = {"result":val}

     resp = make_response(json.dumps(r))
     resp.status_code = 200
     resp.headers['Access-Control-Allow-Origin'] = '*'
     return resp
     

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True)