from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

from pydantic import BaseModel, Field
from datetime import datetime


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load model
model = joblib.load("car_price_model.pkl")



# Input validation model
class CarDetails(BaseModel):

    name: str

    year: int = Field(
        ...,
        ge=1900,
        le=datetime.now().year,
        description="Enter valid car year"
    )

    km_driven: int = Field(
        ...,
        ge=0,
        description="KM driven cannot be negative"
    )

    fuel: str

    transmission: str

    owner: str



@app.get("/")
def home():

    return {
        "message": "Used Car Price Predictor API"
    }



@app.post("/predict")
def predict(car: CarDetails):


    input_data = pd.DataFrame(
        [{
            "name": car.name,
            "year": car.year,
            "km_driven": car.km_driven,
            "fuel": car.fuel,
            "transmission": car.transmission,
            "owner": car.owner
        }]
    )


    prediction = model.predict(input_data)


    return {

        "predicted_price": f"₹ {prediction[0]:,.0f}"

    }