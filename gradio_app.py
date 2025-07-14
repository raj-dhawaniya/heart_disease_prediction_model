import gradio as gr
import numpy as np
import joblib

model = joblib.load("heart_disease_model.pkl")

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg,
                          thalach, exang, oldpeak, slope, ca, thal):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                             thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    return "❤️ Heart Disease Detected" if prediction[0] == 1 else "✅ No Heart Disease"

interface = gr.Interface(
    fn=predict_heart_disease,
    inputs=[
        gr.Number(label="Age"),
        gr.Radio([0, 1], label="Sex (0 = Female, 1 = Male)"),
        gr.Radio([0, 1, 2, 3], label="Chest Pain Type"),
        gr.Number(label="Resting Blood Pressure"),
        gr.Number(label="Cholesterol"),
        gr.Radio([0, 1], label="Fasting Blood Sugar > 120 mg/dl"),
        gr.Radio([0, 1, 2], label="Resting ECG"),
        gr.Number(label="Max Heart Rate Achieved"),
        gr.Radio([0, 1], label="Exercise Induced Angina"),
        gr.Number(label="Oldpeak (ST depression)"),
        gr.Radio([0, 1, 2], label="Slope of ST Segment"),
        gr.Number(label="Number of Major Vessels (0-3)"),
        gr.Radio([0, 1, 2], label="Thal (0 = normal, 1 = fixed defect, 2 = reversible defect)")
    ],
    outputs="text",
    title="❤️ Heart Disease Prediction",
    description="Enter the patient's medical data to predict heart disease."
)

interface.launch(share = True)
