"""
Creator: Morsinaldo Medeiros
Date: 16 Maio 2022
Create API
"""
# from typing import Union
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import pandas as pd
import joblib
import os
import wandb
import sys
from source.api.pipeline import FeatureSelector, CategoricalTransformer, NumericalTransformer

# global variables
setattr(sys.modules["__main__"], "FeatureSelector", FeatureSelector)
setattr(sys.modules["__main__"], "CategoricalTransformer", CategoricalTransformer)
setattr(sys.modules["__main__"], "NumericalTransformer", NumericalTransformer)

# name of the model artifact
artifact_model_name = "risk_credit/model_export:latest"

# initiate the wandb project
run = wandb.init(project="risk_credit",job_type="api")

# create the api
app = FastAPI()

# declare request example data using pydantic
# a person in our dataset has the following attributes
class Person(BaseModel):
    loan_amnt: float
    term: str
    int_rate: float
    installment: float
    emp_lenght: str
    home_ownership: str
    annual_inc: float
    verification_status: str
    purpose: str
    dti: float
    delinq_2yrs: float
    inq_last_6mths: float
    open_acc: float
    pub_rec: float
    revol_bal: float
    revol_util: float
    total_acc: float

    class Config:
        schema_extra = {
            "example": {
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
        }

# give a greeting using GET
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <p><span style="font-size:28px"><strong>Hello World</strong></span></p>"""\
    """<p><span style="font-size:20px">In this project, we will apply the skills """\
        """acquired in the Deploying a Scalable ML Pipeline in Production course to develop """\
        """a classification model on publicly available"""\
        """<a href="http://archive.ics.uci.edu/ml/datasets/Adult"> Census Bureau data</a>.</span></p>"""

# run the model inference and use a Person data structure via POST to the API.
@app.post("/predict")
async def get_inference(person: Person):
    
    # Download inference artifact
    model_export_path = run.use_artifact(artifact_model_name).file()
    pipe = joblib.load(model_export_path)
    
    # Create a dataframe from the input feature
    # note that we could use pd.DataFrame.from_dict
    # but due be only one instance, it would be necessary to
    # pass the Index.
    df = pd.DataFrame([person.dict()])

    # Predict test data
    predict = pipe.predict(df)

    return "Charged Off" if predict[0] <= 0.5 else "Fully Paid"