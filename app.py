import os
from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)


# Load the trained model
model = joblib.load('decision_tree_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        # Extract features from the form data
        age = int(request.form['age'])
        anaemia = int(request.form['anaemia'])
        creatinine_phosphokinase = float(request.form['creatinine_phosphokinase'])
        diabetes = int(request.form['diabetes'])
        ejection_fraction = int(request.form['ejection_fraction'])
        high_blood_pressure = int(request.form['high_blood_pressure'])
        platelets = float(request.form['platelets'])
        serum_creatinine = float(request.form['serum_creatinine'])
        serum_sodium = int(request.form['serum_sodium'])
        sex = int(request.form['sex'])
        smoking = int(request.form['smoking'])
        time = int(request.form['time'])
        
        # Make predictions using the model
        prediction = model.predict([[age, anaemia, creatinine_phosphokinase, diabetes, 
                                      ejection_fraction, high_blood_pressure, platelets, 
                                      serum_creatinine, serum_sodium, sex, smoking, time]])
        
        # Return the prediction as JSON
        if prediction[0] == 1:
            return jsonify({'prediction': 1, 'message': 'The patient is predicted to die'})
        else:
            return jsonify({'prediction': 0, 'message': 'The patient is predicted to survive'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
