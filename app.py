import streamlit as st
import numpy as np

def calculate_ingredient_amounts(rice, fish):
    rice_ratio = 790
    fish_ratio = 209
    supplement_ratio = 18.44
    oil_ratio = 17

    rice_multiplier = rice / rice_ratio
    fish_multiplier = fish / fish_ratio

    min_multiplier = min(rice_multiplier, fish_multiplier)

    rice_used = round(rice_ratio * min_multiplier)
    fish_used = round(fish_ratio * min_multiplier)
    supplement_used = round(supplement_ratio * min_multiplier)
    oil_used = round(oil_ratio * min_multiplier)

    return rice_used, fish_used, supplement_used, oil_used

st.title("Mickéy Fîsh")

rice = st.number_input("Enter the amount of rice (in grams):", min_value=0.0, value=0.0, step=0.1)
fish = st.number_input("Enter the amount of fish (in grams):", min_value=0.0, value=0.0, step=0.1)

if st.button("Calculate"):
    rice_used, fish_used, supplement_used, oil_used = calculate_ingredient_amounts(rice, fish)
    st.write(f"Rice used: {rice_used:.2f} grams")
    st.write(f"Fish used: {fish_used:.2f} grams")
    st.write(f"Supplement used: {supplement_used:.2f} grams")
    st.write(f"Oil used: {oil_used:.2f} grams")
