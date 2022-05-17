"""
Creator: Ivanovitch Silva
Date: 18 April 2022
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
def test_get_inference_low_income():

    person = {
        "age": 72,
        "workclass": 'Self-emp-inc',
        "fnlwgt": 473748,
        "education": 'Some-college',
        "education_num": 10,
        "marital_status": 'Married-civ-spouse',
        "occupation": 'Exec-managerial',
        "relationship": 'Husband',
        "race": 'White',
        "sex": 'Male',
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": 25,
        "native_country": 'United-States'
    }

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "low income <=50K"

# a unit test that tests the status code and response 
# for an instance with a high income
def test_get_inference_high_income():

    person = {
        "age": 46,
        "workclass": 'Private',
        "fnlwgt": 364548,
        "education": 'Bachelors',
        "education_num": 13,
        "marital_status": 'Divorced',
        "occupation": 'Sales',
        "relationship": 'Not-in-family',
        "race": 'White',
        "sex": 'Male',
        "capital_gain": 8614,
        "capital_loss": 0,
        "hours_per_week": 40,
        "native_country": 'United-States'
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "high income >50K"