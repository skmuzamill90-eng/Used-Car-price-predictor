import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.pipeline import Pipeline

from sklearn.metrics import r2_score, mean_absolute_error

import joblib


# ==========================
# Load Dataset
# ==========================

df = pd.read_csv(
    r"C:\Users\skmuz\Downloads\CAR_DETAILS_MODIFIED.csv"
)


# ==========================
# Features and Target
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
# Machine Learning Pipeline
# ==========================

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),

        (
            "regressor",
            RandomForestRegressor(
                n_estimators=300,
                random_state=42
            )
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
# Predictions
# ==========================

predictions = model.predict(X_test)


# ==========================
# Evaluation
# ==========================

r2 = r2_score(
    y_test,
    predictions
)

mae = mean_absolute_error(
    y_test,
    predictions
)

print("R² Score :", round(r2, 3))
print("MAE       :", round(mae, 2))


# ==========================
# Save Model
# ==========================

joblib.dump(
    model,
    "car_price_model.pkl"
)

print("Random Forest model trained successfully")