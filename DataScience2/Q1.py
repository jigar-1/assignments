import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('voice.csv')

# One-hot encoding for the target variable
le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])

# Split into features and target
X = data.drop('label', axis=1)
y = data['label']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initial logistic regression model
lr1 = LogisticRegression(max_iter=1000)
lr1.fit(X_train, y_train)
y_pred1 = lr1.predict(X_test)
acc1 = accuracy_score(y_test, y_pred1)
print(f"Initial Model Accuracy: {acc1:.4f}")

# Compute correlation matrix
corr_matrix = X_train.corr()

# Plot correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', center=0)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Identify highly correlated features (absolute correlation > 0.8)
correlated_features = set()
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            colname = corr_matrix.columns[i]
            correlated_features.add(colname)

# Remove correlated features
X_train_reduced = X_train.drop(correlated_features, axis=1)
X_test_reduced = X_test.drop(correlated_features, axis=1)

# New logistic regression model
lr2 = LogisticRegression(max_iter=1000)
lr2.fit(X_train_reduced, y_train)
y_pred2 = lr2.predict(X_test_reduced)
acc2 = accuracy_score(y_test, y_pred2)
print(f"Reduced Model Accuracy: {acc2:.4f}")

# Compare accuracies
print(f"\nAccuracy Comparison:")
print(f"Initial Model: {acc1:.4f}")
print(f"Reduced Model: {acc2:.4f}")
print(f"Difference: {abs(acc1-acc2):.4f}")