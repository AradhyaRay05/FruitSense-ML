import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
fruit_labels = {
    1: 'Apple',
    2: 'Mandarin',
    3: 'Orange',
    4: 'Lemon'
}

st.title('Fruit Type Prediction App')
st.write('Enter the features of the fruit to predict its type.')

# Input fields for features
mass = st.slider('Mass (g)', 50, 400, 150)
width = st.slider('Width (cm)', 5.0, 10.0, 7.0)
height = st.slider('Height (cm)', 4.0, 12.0, 7.5)
color_score = st.slider('Color Score', 0.5, 1.0, 0.75, 0.01)

if st.button('Predict Fruit Type'):
    input_data = pd.DataFrame([[mass, width, height, color_score]],
                                columns=['mass', 'width', 'height', 'color_score'])

    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)
    predicted_fruit_label = prediction[0]
    predicted_fruit_name = fruit_labels.get(predicted_fruit_label, 'Unknown')

    st.success(f'The predicted fruit type is: **{predicted_fruit_name}**')