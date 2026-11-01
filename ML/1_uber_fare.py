
# Uber Fare Prediction using Linear Regression and Random Forest

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 2. Load Dataset
df = pd.read_csv("uber.csv")
print("Dataset Shape:", df.shape)

# 3. Data Preprocessing
df.drop(columns=["Unnamed: 0", "key"], inplace=True, errors="ignore")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df["pickup_datetime"] = pd.to_datetime(
    df["pickup_datetime"], errors="coerce"
)
df.dropna(subset=["pickup_datetime"], inplace=True)

# Remove invalid records
df = df[
    (df["fare_amount"] > 0) &
    (df["pickup_longitude"].between(-75, -72)) &
    (df["dropoff_longitude"].between(-75, -72)) &
    (df["pickup_latitude"].between(40, 42)) &
    (df["dropoff_latitude"].between(40, 42)) &
    (df["passenger_count"].between(1, 6))
].copy()

# Extract time features
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.day
df["month"] = df["pickup_datetime"].dt.month

df.drop(columns=["pickup_datetime"], inplace=True)

print("Preprocessed Shape:", df.shape)

# 4. Outlier Detection using IQR
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["fare_amount"] < lower) |
    (df["fare_amount"] > upper)
]

print("Number of Outliers:", len(outliers))

sns.boxplot(x=df["fare_amount"])
plt.title("Outlier Detection")
plt.show()

# 5. Correlation Analysis
correlation = df.corr(numeric_only=True)

print("\nCorrelation with Fare Amount:")
print(correlation["fare_amount"].sort_values(ascending=False))

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 6. Split Dataset
X = df.drop(columns=["fare_amount"])
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# 8. Random Forest Regression
rf = RandomForestRegressor(
    n_estimators=100, random_state=42, n_jobs=-1
)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# 9. Model Evaluation
def evaluate(y_test, predictions):

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    return [mae, mse, rmse, r2]


lr_scores = evaluate(y_test, lr_pred)
rf_scores = evaluate(y_test, rf_pred)

# 10. Compare Models
comparison = pd.DataFrame({
    "Linear Regression": lr_scores,
    "Random Forest": rf_scores
}, index=["MAE", "MSE", "RMSE", "R2 Score"])

print("\nModel Comparison:")
print(comparison.round(4))

# 11. Performance Comparison
comparison.loc["R2 Score"].plot(kind="bar")
plt.title("Model Performance Comparison")
plt.ylabel("R2 Score")
plt.show()
