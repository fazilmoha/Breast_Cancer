from flask import request, jsonify
import joblib
import pandas as pd

model = joblib.load('/Users/mdfazil/Desktop/CollegeProject/CollegeProject/BackEnd/Server/Service/Pickle/basic_symptoms_model.pkl')
label_encoder = joblib.load('/Users/mdfazil/Desktop/CollegeProject/CollegeProject/BackEnd/Server/Service/Pickle/basic_symptoms_model.pkl')

def basicSymptoms_Model():
    # Receive JSON request
    json_data = request.json
    


    features = json_data['lump_mass'], json_data['breast_changes'], json_data['skin_changes'], json_data['nipple_changes'], json_data['breast_pain'], json_data['armpit_swelling'], json_data['texture_color_changes'], json_data['nipple_discharge'], json_data['family_history'], json_data['age']
    input_df = pd.DataFrame([features])

    for column in input_df.columns:
        if input_df[column].dtype == 'object':
            input_df[column] = label_encoder.transform(input_df[column])

    prediction = model.predict(input_df)


    predicted_class = label_encoder.inverse_transform(prediction)
    print(predicted_class[0])
    
    response = {'prediction': predicted_class[0]}
    return jsonify(response)