# Purchase_Flask_App
This is a project for our placement traning completion. never mind!!

# 🛍️ VIP Customer Predictor

A Marketing AI tool that predicts whether a customer will purchase a luxury SUV based on their Age and Estimated Salary.

## 🧠 Algorithm
* **Logistic Regression:** A classification algorithm that predicts a binary outcome (1 = Buy, 0 = Don't Buy).

## 📂 Project Structure
* **`model.py`:** Trains the logistic regression model on real user data and saves it.
* **`app.py`:** The Flask server that serves the webpage and processes predictions.
* **`templates/index.html`:** The dark-themed dashboard for marketing inputs.
* **`Social_Network_Ads.csv`:** Real dataset from Kaggle containing user demographics and purchase history.

## 🚀 How to Run
1.  **Install Requirements:**
    ```bash
    pip install pandas flask scikit-learn
    ```
2.  **Train the Model:**
    ```bash
    python model.py
    ```
    *(Check terminal for accuracy score)*
3.  **Start the Web Server:**
    ```bash
    python app.py
    ```
4.  **Open in Browser:**
    Go to `http://127.0.0.1:5000`

## 📊 Dataset
**Source:** [Kaggle - Social Network Ads](https://www.kaggle.com/datasets/rakeshrau/social-network-ads)
* **Inputs:** Age, EstimatedSalary
* **Target:** Purchased (0 or 1)
