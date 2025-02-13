"""
-------------------------------------------------------
====================================================================
                         QuoteAPI - Random Quote Generator
====================================================================

Author:       Naina Vij (HypsyGypsy)
Date:         February 1, 2025
Description:  A simple REST API that returns a random motivational 
              quote from a predefined list. Built using Flask, this 
              API allows users to retrieve quotes by making a GET 
              request to the `/quote` endpoint.

Usage:
    - Run the script: `python3 API.py`
    - Access quotes via: `http://127.0.0.1:5000/quote`

Endpoints:
    - GET `/quote` : Returns a random quote in JSON format.

Example Response:
    {
        "author": "Albert Einstein",
        "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving."
    }

Requirements:
    - Python 3.x
    - Flask (Install using: `pip install flask`)
-------------------------------------------------------
-------------------------------------------------------
"""
# Imports
from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of Quotes
quotes = [
    {"author": "Albert Einstein", "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving."},
    {"author": "Steve Jobs", "quote": "Your time is limited, so don't waste it living someone else's life."},
    {"author": "Maya Angelou", "quote": "Do the best you can until you know better. Then when you know better, do better."},
    {"author": "Confucius", "quote": "It does not matter how slowly you go as long as you do not stop."},
]

@app.route('/quote', methods=['GET'])
def get_random_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)
