import streamlit as st
import math

# Function to calculate piston head thickness based on the provided formula
def calculate_thickness_formula(pressure, diameter, tensile_stress):
    thickness = math.sqrt(3 * pressure * diameter**2 / (16 * tensile_stress))
    return thickness

# Create a Streamlit app
st.title("Piston Head Thickness Calculator")

# Get user input for pressure, piston head diameter, and tensile stress with default values > 0
pressure = st.number_input("Enter pressure on the piston head (in N/mm^2):", value=1.0, min_value=0.1)
piston_diameter = st.number_input("Enter piston head diameter (in mm):", value=10.0, min_value=0.1)
tensile_stress = st.number_input("Enter tensile stress (in N/mm^2):", value=10.0, min_value=0.1)

# Calculate piston head thickness using the formula
thickness_formula = calculate_thickness_formula(pressure, piston_diameter, tensile_stress)

# Display the result
st.write(f"Piston Head Thickness Based on the Provided Formula: {thickness_formula:.2f} mm")
