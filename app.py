# ... (import necessary libraries)
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# Load your trained model (replace 'your_trained_model.pkl' with the actual path)
import pickle

# Load your trained model using pickle
with open('reg_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('preprocessor.pkl', 'rb') as file:
    preprocessor = pickle.load(file)


# ... (import necessary libraries, load the model, and define preprocessing steps)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', results=None)


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Get user input from the form
        gender = request.form['gender']
        ethnicity = request.form['ethnicity']
        parental_education = request.form['parental_level_of_education']
        lunch = request.form['lunch']
        test_course = request.form['test_preparation_course']
        reading_score = float(request.form['reading_score'])
        writing_score = float(request.form['writing_score'])

        # Create a DataFrame with the user input
        input_data = pd.DataFrame({
            'gender': [gender],
            'race_ethnicity': [ethnicity],
            'parental_level_of_education': [parental_education],
            'lunch': [lunch],
            'test_preparation_course': [test_course],
            'reading_score': [reading_score],
            'writing_score': [writing_score]
        })

        # Preprocess the input data (you can reuse your preprocessing code)
        X_input = preprocessor.transform(input_data)
        # Make a prediction using the loaded model
        predicted_math_score = model.predict(X_input)[0]

        # Render the result on the HTML page
        return render_template('result.html', results=predicted_math_score)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
