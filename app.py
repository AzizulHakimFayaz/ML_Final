import gradio as gr
import pandas as pd
import pickle
import numpy as np

<<<<<<< HEAD
# 1. Load your saved Loan Prediction model
with open("Loan.pkl", "rb") as f:
    model = pickle.load(f)

# 2. Define the prediction logic
=======

with open("Loan.pkl", "rb") as f:
    model = pickle.load(f)


>>>>>>> b0a0ccd44e8044d048b6d4d0e2acc439e3ab6a64
def predict_loan(Gender, Married, Dependents, Education, Self_Employed, 
                 ApplicantIncome, CoapplicantIncome, LoanAmount, 
                 Loan_Amount_Term, Credit_History, Property_Area):
    
<<<<<<< HEAD
    # Create a DataFrame for the input
=======

>>>>>>> b0a0ccd44e8044d048b6d4d0e2acc439e3ab6a64
    input_data = pd.DataFrame([[
        Gender, Married, Dependents, Education, Self_Employed,
        ApplicantIncome, CoapplicantIncome, LoanAmount, 
        Loan_Amount_Term, Credit_History, Property_Area
    ]], columns=[
        'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 
        'Loan_Amount_Term', 'Credit_History', 'Property_Area'
    ])
    
<<<<<<< HEAD
    # Apply One-Hot Encoding as done in your training script
    # Note: X = pd.get_dummies(X, drop_first=True) was used
    input_encoded = pd.get_dummies(input_data, drop_first=True)
    
    # Align columns with the model's expected features
    model_features = model.feature_names_in_
    input_final = input_encoded.reindex(columns=model_features, fill_value=0)
    
    # Predict status
    prediction = model.predict(input_final)[0]
    
    if prediction == 'Y':
        return "✅ APPROVED: The applicant is likely eligible for the loan."
    else:
        return "❌ REJECTED: The applicant is unlikely to be eligible."

# 3. Setup the Gradio Interface
=======

    input_encoded = pd.get_dummies(input_data, drop_first=True)
    

    model_features = model.feature_names_in_
    input_final = input_encoded.reindex(columns=model_features, fill_value=0)
    

    prediction = model.predict(input_final)[0]
    
    if prediction == 'Y':
        return " APPROVED: The applicant is likely eligible for the loan."
    else:
        return " REJECTED: The applicant is unlikely to be eligible."


>>>>>>> b0a0ccd44e8044d048b6d4d0e2acc439e3ab6a64
inputs = [
    gr.Dropdown(["Male", "Female"], label="Gender"),
    gr.Dropdown(["Yes", "No"], label="Married"),
    gr.Dropdown(["0", "1", "2", "3+"], label="Dependents"),
    gr.Dropdown(["Graduate", "Not Graduate"], label="Education"),
    gr.Dropdown(["Yes", "No"], label="Self Employed"),
    gr.Number(label="Applicant Income", value=5000),
    gr.Number(label="Co-applicant Income", value=0),
    gr.Number(label="Loan Amount", value=150),
    gr.Number(label="Loan Term (Days)", value=360),
    gr.Dropdown([1.0, 0.0], label="Credit History"),
    gr.Dropdown(["Urban", "Semiurban", "Rural"], label="Property Area")
]

app = gr.Interface(
    fn=predict_loan,
    inputs=inputs,
    outputs="text",
    title="Loan Eligibility Prediction Tool",
    description="Predict whether a loan will be approved based on applicant details."
)

<<<<<<< HEAD
# 4. Launch the application
=======

>>>>>>> b0a0ccd44e8044d048b6d4d0e2acc439e3ab6a64
app.launch(share=True)