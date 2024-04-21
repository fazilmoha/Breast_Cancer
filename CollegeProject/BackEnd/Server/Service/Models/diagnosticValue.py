from flask import request, jsonify
import joblib
import pandas as pd

model = joblib.load('/Users/mdfazil/Desktop/CollegeProject/CollegeProject/BackEnd/Server/Service/Pickle/diagnostic_model.pkl')

def diagnosticValue():
    # Receive JSON request
    json_data = request.json
    
    features = json_data['texture_mean'], json_data['smoothness_mean'], json_data['compactness_mean'], json_data['concave_points_mean'], json_data['symmetry_mean'], json_data['fractal_dimension_mean'], json_data['texture_se'], json_data['area_se'], json_data['smoothness_se'], json_data['compactness_se'], json_data['concavity_se'], json_data['concave_points_se'], json_data['symmetry_se'], json_data['fractal_dimension_se'],json_data['texture_worst'],json_data['area_worst'],json_data['smoothness_worst'],json_data['compactness_worst'],json_data['concavity_worst'],json_data['concave_points_worst'],json_data['symmetry_worst'],json_data['fractal_dimension_worst']
    input_df = pd.DataFrame([features])

    prediction = model.predict(input_df)
    print("prediction")
    
    if(prediction[0] == 0):
        val = 'B'
    elif(prediction[0] == 1):
        val = 'M'
    else:
        val = "Model Error"
    data = {
        'Result' : val
    }
    print(val)
    return jsonify(data)