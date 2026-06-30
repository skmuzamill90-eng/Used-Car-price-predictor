import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.pipeline import Pipeline

import joblib


# ==========================
# Load Dataset
# ==========================

df = pd.read_csv(
    r"C:\Users\skmuz\Downloads\CAR_DETAILS_MODIFIED.csv"
)


# ==========================
# Separate Features and Target
# ==========================

X = df.drop("selling_price", axis=1)

y = df["selling_price"]



# ==========================
# Categorical Columns
# ==========================

categorical_columns = [
    "name",
    "fuel",
    "transmission",
    "owner"
]



# ==========================
# Preprocessing
# ==========================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)



# ==========================
# Create ML Pipeline
# ==========================

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),

        (
            "regressor",
            LinearRegression()
        )
    ]
)



# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# ==========================
# Train Model
# ==========================

model.fit(
    X_train,
    y_train
)



# ==========================
# Check Accuracy
# ==========================

score = model.score(
    X_test,
    y_test
)

print("Model Accuracy:", score)



# ==========================
# Save Model
# ==========================

joblib.dump(
    model,
    "car_price_model.pkl"
)


print("Model trained and saved successfully")