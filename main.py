from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model
model = joblib.load("car_price_model.pkl")

# Load encoders
name_encoder = joblib.load("name_encoder.pkl")

fuel_encoder = joblib.load("fuel_encoder.pkl")

transmission_encoder = joblib.load(
    "transmission_encoder.pkl"
)

owner_encoder = joblib.load(
    "owner_encoder.pkl"
)

# Home route
@app.get("/")
def home():

    return {
        "message": "Used Car Price Predictor API"
    }

# Prediction route
@app.get("/predict")
def predict(
    name: str,
    year: int,
    km_driven: int,
    fuel: str,
    transmission: str,
    owner: str
):

    # Encode inputs
    name = name_encoder.transform([name])[0]

    fuel = fuel_encoder.transform([fuel])[0]

    transmission = transmission_encoder.transform(
        [transmission]
    )[0]

    owner = owner_encoder.transform([owner])[0]

    # Predict price
    prediction = model.predict([[
        name,
        year,
        km_driven,
        fuel,
        transmission,
        owner
    ]])

    # Return result
    return {
        "predicted_price": round(
            prediction[0],
            2
        )
    }