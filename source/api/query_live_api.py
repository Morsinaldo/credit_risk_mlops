"""
Creator: Morsinaldo Medeiros and Alessandro Neto
Date: 16 Maio de 2022
Script that POSTS to the API using the requests 
module and returns both the result of 
model inference and the status code
"""
import requests
import json
# import pprint

person = {
        "loan_amnt": 5000.0,
        "term": '36 months',
        "int_rate": 5,
        "installment": 162.87,
        "emp_length": "10+ years",
        "home_ownership": "RENT",
        "annual_inc": 24000,
        "verification_status": "Verified",
        "purpose": "car",
        "dti": 27.65,
        "delinq_2yrs": 0.0,
        "inq_last_6mths": 1.0,
        "open_acc": 3.0,
        "pub_rec": 0.0,
        "revol_bal": 13648.0,
        "revol_util": 83.7,
        "total_acc": 9.0
    }

#url = "http://127.0.0.1:8000"
url = "https://risk-credit-mlops.herokuapp.com"
response = requests.post(f"{url}/predict",json=person)

print(f"Request: {url}/predict")
print(f"Person: \n loan_amnt: {person['loan_amnt']}\n term: {person['term']}\n"\
      f" int_rate: {person['int_rate']}\n installment: {person['installment']}\n"\
      f" emp_length: {person['emp_length']}\n"\
      f" home_ownership: {person['home_ownership']}\n"\
      f" annual_inc: {person['annual_inc']}\n"\
      f" verification_status: {person['verification_status']}\n"\
      f" purpose: {person['purpose']}\n"\
      f" dti: {person['dti']}\n"\
      f" delinq_2yrs: {person['delinq_2yrs']}\n"\
      f" inq_last_6mths: {person['inq_last_6mths']}\n"\
      f" open_acc: {person['open_acc']}\n"\
      f" pub_rec: {person['pub_rec']}\n"\
      f" revol_bal: {person['revol_bal']}\n"\
      f" revol_util: {person['revol_util']}\n"\
      f" total_acc: {person['total_acc']}\n"
     )
print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")