from flask import Flask, request, jsonify
from plaid.api import plaid_api
from plaid.model.country_code import CountryCode
from plaid.model.products import Products
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

import plaid
from plaid.api import plaid_api

app = Flask(__name__)

client_id = os.getenv('PLAID_CLIENT_ID')
secret_id = os.getenv('PLAID_SECRET')

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret_id,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

@app.route('/create_link_token', methods=['POST'])
def create_link_token():
    try:
        request = LinkTokenCreateRequest(
            products=[Products("transactions")],
            client_name="me",
            country_codes=[CountryCode("US")],
            language="en",
            user=LinkTokenCreateRequestUser(client_user_id="unique-user-id")
        )
        response = client.link_token_create(request)
        return jsonify(response.to_dict())
    except plaid.ApiException as e:
        return jsonify({'error': e.body})

@app.route('/exchange_public_token', methods=['POST'])
def exchange_public_token():
    data = request.get_json()
    public_token = data.get('public_token')

    if not public_token:
        return jsonify({'error': 'Missing public token'}), 400

    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )

    try:
        exchange_response = client.item_public_token_exchange(exchange_request)
        access_token = exchange_response['access_token']
        return jsonify({'access_token': access_token})
    except plaid.ApiException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_transactions', methods=['POST'])
def get_transactions():
    data = request.get_json()
    if not data or 'access_token' not in data:
        return jsonify({'error': 'Missing access_token'}), 400

    access_token = data['access_token']

    # Setup the dates for fetching transactions
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    try:
        transactions_request = {
            'access_token': access_token,
            'start_date': start_date,
            'end_date': end_date,
        }
        
        response = client.transactions_get(transactions_request)
        return jsonify(response.to_dict())
    except plaid.ApiException as e:
        return jsonify({'error': str(e)})