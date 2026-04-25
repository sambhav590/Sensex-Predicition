from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # CORS allow (frontend connect karega)

# 🔴 Live Sensex API
@app.route('/sensex')
def get_sensex():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5EBSESN"
        response = requests.get(url)
        data = response.json()

        price = data['quoteResponse']['result'][0]['regularMarketPrice']

        return jsonify({
            "status": "success",
            "price": price
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "price": "Not Available"
        })


# 🟢 Home route (optional check)
@app.route('/')
def home():
    return "Sensex API Running ✅"


# ▶️ Run server
if __name__ == '__main__':
    app.run(debug=True)