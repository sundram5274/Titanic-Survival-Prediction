# app.py
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("titanicPrediction.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        Pclass = int(request.form['Pclass'])
        Sex = 1 if request.form['Sex'] == 'female' else 0
        Age = float(request.form['Age'])

        # Convert fare range to float
        fare_input = request.form['Fare']
        fare_map = {
            "0-7": 3.5,
            "8-20": 14,
            "21-40": 30.5,
            "41+": 60
        }
        Fare = fare_map.get(fare_input, 14)

        Embarked = {'S': 0, 'C': 1, 'Q': 2}[request.form['Embarked']]
        SibSp = int(request.form['SibSp'])
        Parch = int(request.form['Parch'])

        features = np.array([[Pclass, Sex, Age, Fare, Embarked, SibSp, Parch]])
        prediction = model.predict(features)[0]

        result = "Survived" if prediction == 1 else "Did Not Survive"
        return render_template('index.html', prediction_text=f"Prediction: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
