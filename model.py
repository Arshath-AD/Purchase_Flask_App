import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

# 1. Load the REAL dataset from Kaggle
# Make sure the file name matches exactly what you downloaded!
df = pd.read_csv('Social_Network_Ads.csv')

# 2. Select Features (X) and Target (y)
# The columns in this dataset are usually: 'Age', 'EstimatedSalary', 'Purchased'
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# 3. Train the Logistic Regression Model
classifier = LogisticRegression()
classifier.fit(X, y)

# 4. Save the model
pickle.dump(classifier, open('model.pkl', 'wb'))

print("Success! Trained on Social_Network_Ads.csv and saved model.pkl")
print("Model Score (Accuracy):", classifier.score(X, y))