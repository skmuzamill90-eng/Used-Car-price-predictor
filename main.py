from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

from pydantic import BaseModel, Field
from datetime import datetime


# ==========================
# Create FastAPI App
# ==========================

app = FastAPI()


# ==========================
# Enable CORS
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================
# Load Trained Model
# ==========================

model = joblib.load("car_price_model.pkl")


# ==========================
# Indian Currency Formatter
# ==========================

def format_indian_currency(number):

    number = int(round(number))

    s = str(number)

    if len(s) <= 3:
        return s

    last_three = s[-3:]
    remaining = s[:-3]

    result = ""

    while len(remaining) > 2:

        result = "," + remaining[-2:] + result

        remaining = remaining[:-2]

    result = remaining + result

    return result + "," + last_three


# ==========================
# Input Validation
# ==========================

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
        description="KM Driven cannot be negative"
    )

    fuel: str

    transmission: str

    owner: str


# ==========================
# Home API
# ==========================

@app.get("/")
def home():

    return {
        "message": "Used Car Price Predictor API"
    }


# ==========================
# Prediction API
# ==========================

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

    # Predict Price
    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    # Calculate ±10% Range
    lower_price = predicted_price * 0.90
    upper_price = predicted_price * 1.10

    return {

        "predicted_price":
        f"₹ {format_indian_currency(lower_price)} - ₹ {format_indian_currency(upper_price)}"

    }