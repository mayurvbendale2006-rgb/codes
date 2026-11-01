
# Email Spam Detection using KNN and SVM

# 1. Import Libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 2. Load Dataset
df = pd.read_csv("emails.csv")

print("Original Dataset Shape:", df.shape)

# 3. Data Preprocessing
df = df.dropna()

print("Dataset Shape after removing missing values:", df.shape)

# Remove Email Number column
df = df.drop(columns=["Email No."])

# Separate features and target
X = df.drop(columns=["Prediction"])
y = df["Prediction"].astype(int)

print("\nTarget Distribution:")
print(y.value_counts())

# Check binary target
if set(y.unique()) != {0, 1}:
    print("Error: Prediction must contain both 0 and 1")
else:

    # 4. Split Dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 5. Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 6. KNN Classification
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    knn_pred = knn.predict(X_test)

    # 7. SVM Classification
    svm = SVC(kernel="linear")
    svm.fit(X_train, y_train)

    svm_pred = svm.predict(X_test)

    # 8. Model Evaluation
    print("\nKNN Results")
    print("Accuracy:", accuracy_score(y_test, knn_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, knn_pred))
    print(classification_report(y_test, knn_pred))

    print("\nSVM Results")
    print("Accuracy:", accuracy_score(y_test, svm_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, svm_pred))
    print(classification_report(y_test, svm_pred))

    # 9. Performance Comparison
    comparison = pd.DataFrame({
        "KNN": [accuracy_score(y_test, knn_pred)],
        "SVM": [accuracy_score(y_test, svm_pred)]
    }, index=["Accuracy"])

    print("\nPerformance Comparison:")
    print(comparison)
