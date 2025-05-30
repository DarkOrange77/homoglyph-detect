# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from homoglyph_utils import detect_homoglyphs

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    text = data.get('text', '')
    result = detect_homoglyphs(text)
    return jsonify(result)

@app.route('/')
def home():
    return "Homoglyph Detect API is running! Use POST /detect."

if __name__ == '__main__':
    app.run(debug=True)
    