import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("loan_borowwer_data.csv")

# Preprocessing
le = LabelEncoder()
df['purpose'] = le.fit_transform(df['purpose'])

# Features and target
X = df.drop('not.fully.paid', axis=1)
y = df['not.fully.paid']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))