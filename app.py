from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return '<h1>Hiya</h1>'

@app.route('/about')
def about():
    return '<h3>I am a programmer</h3>'

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == "__main__": 
    app.run(debug=True) 