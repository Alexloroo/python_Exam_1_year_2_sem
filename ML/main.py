import joblib
import json
import sklearn as sk
import pandas as pd
import sys
from pydantic import BaseModel

from fastapi import FastAPI
app = FastAPI()


model = joblib.load("linear_model.joblib")
mp = {'no': 0, 'yes': 1, 'furnished': 1, 'semi-furnished': 0.5, 'unfurnished': 0}
clas = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']

class HouseInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    parking: int
    prefarea: str
    furnishingstatus: str

@app.post("/predict")
def predict(input: HouseInput):
    df = pd.DataFrame([input.dict()])

    for i in clas:
        df[i] = df[i].map(mp)
    return {"pred" :round(int(model.predict(df)[0]), -2)}