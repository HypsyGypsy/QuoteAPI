"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2025-02-12"
-------------------------------------------------------
"""
# Imports

# Constants

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
