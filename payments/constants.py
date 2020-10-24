import requests
from requests.auth import HTTPBasicAuth

business_short_code = "174379"#for test env
phone_making_payment = "254743970626"
lipa_na_mpesa_pass_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
app_consumer_key = "CEWwwETv9tA73Ct9poNq4QRP6xbg3wAK"
app_consumer_secret = "fl4DgiIuSRqdRoN7"


#Here we are generating the access token

consumer_key = app_consumer_key
consumer_secret = app_consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

#print (r.text)
json_response = r.json()

my_access_token = json_response['access_token']