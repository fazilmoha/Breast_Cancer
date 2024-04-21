from flask import Flask
from flask_cors import CORS

from Service.GetHospital.getHospital import getHospitals
from Service.Login.login import login
from Service.SignUp.signUp import signUp
from Service.Models.basicSymptom import basicSymptoms_Model
from Service.Models.diagnosticValue import diagnosticValue

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

# Signup endpoint
@app.route('/signup', methods=['POST'])
def signup():
    return signUp()

# Login endpoint
@app.route('/login', methods=['POST'])
def login_Controller():
    return login()
   
@app.route('/basic_symptoms', methods=['POST'])
def receive_data():
    return basicSymptoms_Model()

@app.route('/diagnostic_value', methods=['POST'])
def receive_data_model2():
    return diagnosticValue()

@app.route('/hospitals', methods=['GET'])
def get_hospitals_Controller():
    return getHospitals()


if __name__ == '__main__':
    app.run(debug=True)
