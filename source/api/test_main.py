"""
Creator: Morsinaldo Medeiros
Date: 17 Maio 2022
API testing
"""
from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with a low income
def test_get_inference_fully_paid():

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

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "Fully Paid"

# a unit test that tests the status code and response 
# for an instance with a high income
def test_get_inference_charged_off():

    person = {
        "loan_amnt": 21000.0,
        "term": '36 months',
        "int_rate": 12.42,
        "installment": 701.73,
        "emp_length": "10+ years",
        "home_ownership": "RENT",
        "annual_inc": 105000,
        "verification_status": "Verified",
        "purpose": "debt_consolidation",
        "dti": 13.22,
        "delinq_2yrs": 0.0,
        "inq_last_6mths": 0.0,
        "open_acc": 7.0,
        "pub_rec": 0.0,
        "revol_bal": 32135.0,
        "revol_util": 90.3,
        "total_acc": 38.0
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Charged Off"