import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# 1. Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get Age and Salary from the form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # 2. Predict (Returns [0] or [1])
    prediction = model.predict(final_features)
    
    # 3. Format result
    if prediction[0] == 1:
        result = "YES! Target Customer (Likely to Buy) 💰"
        color = "green"
    else:
        result = "NO. Not a Target Customer ❌"
        color = "red"

    return render_template('index.html', prediction_text=result, result_color=color)

if __name__ == "__main__":
    app.run(debug=True)