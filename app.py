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

    min_multiplier_int = int(min_multiplier)
    
    # Find the smallest integer multiplier that results in integer amounts for all ingredients
    while True:
        rice_used = rice_ratio * min_multiplier_int
        fish_used = fish_ratio * min_multiplier_int
        supplement_used = supplement_ratio * min_multiplier_int
        oil_used = oil_ratio * min_multiplier_int

        if (rice_used.is_integer() and fish_used.is_integer() and
            supplement_used.is_integer() and oil_used.is_integer()):
            break
        else:
            min_multiplier_int -= 1

    return rice_used, fish_used, supplement_used, oil_used
