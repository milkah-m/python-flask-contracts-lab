#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to Contract Hub!<h1>'

@app.route('/contract/<id>')
def contract(id):
    contract_ids = [contract['id'] for contract in contracts]
    if int(id) not in contract_ids:
        return make_response("", 404, {})
    contract_information = [contract['contract_information'] for contract in contracts if contract['id'] == int(id)]
    return make_response(contract_information[0], 200, {})

@app.route('/customer/<customer_name>')
def customer(customer_name):
    if customer_name not in customers:
        return make_response("", 404, {})
    return make_response("", 204, {})

if __name__ == '__main__':
    app.run(port=5555, debug=True)


