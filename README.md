# Titanic-Survival-Prediction
This project uses machine learning to predict whether a passenger on the Titanic would have survived based on features like age, sex, class, fare, and embarkation point. It includes model training, evaluation, and a simple Flask web app for live prediction.

🔍 **Project Overview**

Dataset: Titanic dataset from Kaggle

Goal: Predict survival of a passenger based on input features

Models Used:

Logistic Regression
Random Forest Classifier ✅ (best performance)

📁 **Project Structure**
titanic-survival-prediction/
├── static/
│   └── style.css             # CSS for styling the form
├── templates/
│   └── index.html            # Frontend input form
├── train.csv                 # Training data
├── test.csv                  # Test data
├── Untitled.ipynb            # Jupyter notebook (model building)
├── titanicPrediction.pkl     # Saved Random Forest model
└── app.py                    # Flask web app

🔧**Tech Stack**

Python
Pandas, NumPy
Scikit-learn
Flask
HTML & CSS

📊 **Model Evaluation**

Model                  Accuracy

Logistic Regression    ~78%
Random Forest          ~82% ✅

Random Forest outperformed Logistic Regression and was used for final deployment.

🌐 **Deployment with Flask**

A Flask app was created with an HTML form where users can input features like:

Passenger class

Sex

Age

Fare (categorized as Low, Medium, High, Very High)

Embarked location

The model takes these inputs and returns whether the passenger would have Survived or Not Survived.

▶️ **How to Run Locally**

Clone the repository:

git clone https://github.com/sundram5274/titanic-survival-prediction.git

cd titanic-survival-prediction

Install dependencies:

pip install -r requirements.txt

Run the app:

python app.py

Open http://127.0.0.1:5000 in your browser

💡 **Future Improvements**

Add more features (e.g. family size)

Host the app on Render/Heroku

Add better error handling and UI








