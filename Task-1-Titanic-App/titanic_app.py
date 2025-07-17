import streamlit as st
import pandas as pd
import joblib

st.title("🚢 Titanic Survival Prediction")
st.markdown("Choose a model and enter passenger details to predict survival.")

# Load models
rf_model = joblib.load("rf_model.pkl")
logreg_model = joblib.load("logreg_model.pkl")

# Model selector
model_choice = st.selectbox("Select Model", ["Random Forest", "Logistic Regression"])

# Input fields
Pclass = st.selectbox("Ticket Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.slider("Age", 0, 80, 25)
Fare = st.slider("Fare", 0.0, 500.0, 32.2)
FamilySize = st.slider("Family Size", 1, 10, 1)
Embarked_S = st.checkbox("Embarked from Southampton?")
Embarked_Q = st.checkbox("Embarked from Queenstown?")
IsAlone = 1 if FamilySize == 1 else 0
Sex = 0 if Sex == 'male' else 1

if st.button("Predict Survival"):
    input_data = pd.DataFrame({
        'Pclass': [Pclass],
        'Sex': [Sex],
        'Age': [Age],
        'Fare': [Fare],
        'FamilySize': [FamilySize],
        'IsAlone': [IsAlone],
        'Embarked_Q': [1 if Embarked_Q else 0],
        'Embarked_S': [1 if Embarked_S else 0],
    })

    model = rf_model if model_choice == "Random Forest" else logreg_model
    prediction = model.predict(input_data)
    result = "🟢 Survived" if prediction[0] == 1 else "🔴 Did Not Survive"
    
    st.subheader("Prediction Result:")
    st.success(result)
