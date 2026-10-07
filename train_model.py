import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# Load dataset
df = pd.read_csv("data/laptop_data.csv")

print("Dataset loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# Features and target
X = df.drop("Price_INR", axis=1)
y = df["Price_INR"]


# Identify categorical and numerical columns
categorical_columns = X.select_dtypes(
    include=["object"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    exclude=["object"]
).columns.tolist()


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        (
            "numerical",
            "passthrough",
            numerical_columns
        )
    ]
)


# Machine Learning model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)


# Complete pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
pipeline.fit(X_train, y_train)

print("Model training completed")


# Predictions
predictions = pipeline.predict(X_test)


# Model evaluation
mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)


print("\nModel Evaluation")
print("----------------")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 4))


# Save trained model
with open(
    "laptop_price_model.pkl",
    "wb"
) as file:
    pickle.dump(pipeline, file)


print("\nModel saved as laptop_price_model.pkl")