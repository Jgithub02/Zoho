from flask import Flask, render_template, redirect, request, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Home route
@app.route('/')
def homepage():
    return render_template('contract_template.html')

# OAuth callback route
@app.route('/oauth/callback')
def oauth_callback():
    # Get authorization code
    code = request.args.get('code')
    # Exchange code for access token
    token_url = 'https://accounts.zoho.com/oauth/v2/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': os.getenv('ZOHO_CLIENT_ID'),
        'client_secret': os.getenv('ZOHO_CLIENT_SECRET'),
        'redirect_uri': os.getenv('ZOHO_REDIRECT_URI'),
        'code': code
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    # Save access_token for later use
    # (You would typically store this in a secure way)
    return redirect(url_for('homepage'))

# Initiate signing process
@app.route('/sign', methods=['POST'])
def initiate_signing():
    # Send contract to Zoho Sign API
    # For example: setup payload and send request
    return "Signing initiated!"

# Webhook for signature completion
@app.route('/webhook', methods=['POST'])
def webhook():
    # Handle webhook notifications from Zoho Sign
    data = request.json
    # Process the data (e.g., update contract status)
    return "Webhook received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

