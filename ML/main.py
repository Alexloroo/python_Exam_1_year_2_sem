import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

model = joblib.load("linear_model.joblib")

mp = {
    'no': 0,
    'yes': 1,
    'furnished': 1,
    'semi-furnished': 0.5,
    'unfurnished': 0
}

yes_no_fields = [
    'mainroad',
    'guestroom',
    'basement',
    'hotwaterheating',
    'airconditioning',
    'prefarea'
]

class HouseInput(BaseModel):
    area: float = Field(..., gt=0)
    bedrooms: int = Field(..., ge=1, le=20)
    bathrooms: int = Field(..., ge=1, le=20)
    stories: int = Field(..., ge=1, le=10)
    parking: int = Field(..., ge=0, le=10)

    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    prefarea: str

    furnishingstatus: str

    @field_validator(
        'mainroad',
        'guestroom',
        'basement',
        'hotwaterheating',
        'airconditioning',
        'prefarea'
    )
    @classmethod
    def validate_yes_no(cls, value):
        if value not in ['yes', 'no']:
            raise ValueError("Значение должно быть 'yes' или 'no'")
        return value

    @field_validator('furnishingstatus')
    @classmethod
    def validate_furnishing(cls, value):
        allowed = ['furnished', 'semi-furnished', 'unfurnished']

        if value not in allowed:
            raise ValueError(
                f"furnishingstatus должен быть одним из: {allowed}"
            )

        return value


@app.post("/predict")
def predict(input: HouseInput):
    df = pd.DataFrame([input.model_dump()])

    for col in yes_no_fields:
        df[col] = df[col].map(mp)

    df['furnishingstatus'] = df['furnishingstatus'].map(mp)

    prediction = model.predict(df)[0]

    return {
        "pred": round(int(prediction), -2)
    }