import requests
import constants#file containing constatnts
import base64
from datetime import datetime as dt

print(dt.now())
unformated_time = dt.now()
formated_time = unformated_time.strftime("%Y%m%d%H%M%S")

data_to_encode = constants.business_short_code + constants.lipa_na_mpesa_pass_key + formated_time
  #combines three string the buss_short_code+lipa_na_mpesa_pass_key+timestamp

encoded_pass_value = base64.b64encode(data_to_encode.encode())# generate the password value
decoded_pass_value = encoded_pass_value.decode('utf-8')

print(decoded_pass_value)


def lipa_na_mpesa_base_function(): 
    access_token = constants.my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": constants.business_short_code,#busiss paybill or buy goods number
        "Password": decoded_pass_value,#password for encrypting request
        "Timestamp": formated_time,#YYYYMMDDHHMMSS
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "2",#how much is to be paid
        "PartyA": constants.phone_making_payment,#client phone number or phone number sending the money
        "PartyB": constants.business_short_code,#busiss paybill or buy goods number
        "PhoneNumber": constants.phone_making_payment,#client phone number or phone number sending the money
        "CallBackURL": "https://intelcx.com",
        "AccountReference": "SCII/02138/2016",#client identifier e.g account number
        "TransactionDesc": "IntelCx Course Payments"#what is being paid for
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

lipa_na_mpesa_base_function()