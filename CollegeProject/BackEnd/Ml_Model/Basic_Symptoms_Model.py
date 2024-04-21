import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import shap
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/mdfazil/Desktop/CollegeProject/CollegeProject/BackEnd/DataSet/basic_symptoms.csv')

# Encode categorical variables
label_encoder = LabelEncoder()
df['Diagnosis'] = label_encoder.fit_transform(df['Diagnosis'])

label_encoder = LabelEncoder()
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = label_encoder.fit_transform(df[column])
        
# Split features (X) and target variable (y)
X = df.drop(columns=['Patient ID', 'Diagnosis'])
y = df['Diagnosis']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a basic Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# # Collect input from the user
# input_data = {
#     'Lump/Mass': input("Lump/Mass (Yes/No): "),
#     'Breast Changes': input("Breast Changes (Yes/No): "),
#     'Skin Changes': input("Skin Changes (Yes/No): "),
#     'Nipple Changes': input("Nipple Changes (Yes/No): "),
#     'Breast Pain': input("Breast Pain (Yes/No): "),
#     'Armpit Swelling': input("Armpit Swelling (Yes/No): "),
#     'Texture/Color Changes': input("Texture/Color Changes (Yes/No): "),
#     'Nipple Discharge': input("Nipple Discharge (Yes/No): "),
#     'Family History': input("Family History (Yes/No): "),
#     'Age': int(input("Age: "))
# }

# # Convert input into DataFrame
# input_df = pd.DataFrame([input_data])

# # Preprocess input data
# for column in input_df.columns:
#     if input_df[column].dtype == 'object':
#         input_df[column] = label_encoder.transform(input_df[column])

# # Make prediction
# prediction = clf.predict(input_df)

# # Convert the predicted label back to original class
# predicted_class = label_encoder.inverse_transform(prediction)

# # Display prediction
# print("Predicted Diagnosis:", predicted_class[0])
# Create a SHAP explainer
explainer = shap.Explainer(clf, X_train)
shap_values = explainer.shap_values(X_test)

# Visualize the summary plot
shap.summary_plot(shap_values, X_test, plot_type="bar")
#plt.savefig('/Users/mdfazil/Desktop/CollegeProject/CollegeProject/Image/image1.png')

joblib.dump(clf, '/Users/mdfazil/Desktop/CollegeProject/CollegeProject/BackEnd/Ml_Model/model.pkl')
joblib.dump(label_encoder, '/Users/mdfazil/Desktop/CollegeProject/CollegeProject/BackEnd/Ml_Model/label_encode.pkl')