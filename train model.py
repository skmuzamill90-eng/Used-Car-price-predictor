import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv(r"C:\Users\skmuz\Downloads\CAR DETAILS FROM CAR DEKHO.csv")

# Create encoders
name_encoder = LabelEncoder()
fuel_encoder = LabelEncoder()
transmission_encoder = LabelEncoder()
owner_encoder = LabelEncoder()

# Encode categorical columns
df["name"] = name_encoder.fit_transform(df["name"])

df["fuel"] = fuel_encoder.fit_transform(df["fuel"])

df["transmission"] = transmission_encoder.fit_transform(
    df["transmission"]
)

df["owner"] = owner_encoder.fit_transform(df["owner"])

# Features
X = df[[
    "name",
    "year",
    "km_driven",
    "fuel",
    "transmission",
    "owner"
]]

# Target
y = df["selling_price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "car_price_model.pkl")

# Save encoders
joblib.dump(name_encoder, "name_encoder.pkl")

joblib.dump(fuel_encoder, "fuel_encoder.pkl")

joblib.dump(
    transmission_encoder,
    "transmission_encoder.pkl"
)

joblib.dump(owner_encoder, "owner_encoder.pkl")

print("Model trained successfully")