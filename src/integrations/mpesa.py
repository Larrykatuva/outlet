from outlet.settings import (
    MPESA_SANDBOX,
    MPESA_PASSKEY,
    MPESA_PASSWORD,
    MPESA_CALLBACK,
    MPESA_USERNAME,
    MPESA_LIPA_NA_MPESA_URL,
    MPESA_ACCESS_TOKEN_URL,
    MPESA_BUSINESS_SHORT_CODE,
)
import requests
import json
from datetime import datetime

import base64


class MpesaPayment:

    @staticmethod
    def get_access_token() -> json:
        response = requests.get(
            MPESA_ACCESS_TOKEN_URL,
            auth=requests.auth.HTTPBasicAuth(
                MPESA_USERNAME,
                MPESA_PASSWORD
            )
        )
        return response.json()

    @staticmethod
    def generate_password() -> tuple:
        unformatted_time = datetime.now()
        formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
        data_to_encode = MPESA_BUSINESS_SHORT_CODE + MPESA_PASSKEY + formatted_time
        print(data_to_encode)
        encoded_string = base64.b64encode(data_to_encode.encode())
        decoded_password = encoded_string.decode('utf-8')
        return decoded_password, formatted_time

    def lipa_na_mpesa(
            self,
            amount: int,
            phone: str,
            transaction_desc: str
    ) -> json:
        access_token = self.get_access_token().get('access_token')
        password, timestamp = self.generate_password()
        headers = {"Authorization": "Bearer %s" % access_token}
        body = {
            "BusinessShortCode": MPESA_BUSINESS_SHORT_CODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 1,
            "PartyA": phone,
            "PartyB": MPESA_BUSINESS_SHORT_CODE,
            "PhoneNumber": phone,
            "CallBackURL": MPESA_CALLBACK + "/order/call-back",
            "AccountReference": "CompanyXLTD",
            "TransactionDesc": transaction_desc
        }

        print(body)
        response = requests.post(
            MPESA_LIPA_NA_MPESA_URL,
            json=body,
            headers=headers
        )
        return response.json()
