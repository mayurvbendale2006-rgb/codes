
# Bank Customer Churn Prediction using ANN

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Load dataset
df = pd.read_csv("Churn_Modelling.csv")

print("Dataset Shape:", df.shape)

# 2. Remove unnecessary columns
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# 3. Encode categorical columns
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True, dtype=int)

# 4. Separate features and target
X = df.drop("Exited", axis=1)
y = df["Exited"]

# 5. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7. Create ANN model
model = Sequential()

model.add(Dense(16, activation="relu", input_shape=(X_train.shape[1],)))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

# 8. Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# 9. Train model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# 10. Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print("\nTest Accuracy:", accuracy)

# 11. Make predictions
y_pred = (model.predict(X_test) > 0.5).astype(int)

# 12. Display results
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
