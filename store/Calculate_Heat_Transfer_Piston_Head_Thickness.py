import streamlit as st
import math

# Function to calculate piston head thickness based on the provided heat transfer formula
def calculate_thickness_heat_transfer(H, K, temperature_center, temperature_edge):
    thickness = H / (12.56 * K * (temperature_center - temperature_edge))
    return thickness

# Create a Streamlit app
st.title("Piston Head Thickness Calculator - Heat Transfer")

# Get user input for H, K, temperature at the center, and temperature at the edge with default values > 0
H = st.number_input("Enter H (heat transfer coefficient):", value=1.0, min_value=0.1)
K = st.number_input("Enter K (thermal conductivity of the material):", value=1.0, min_value=0.1)
temperature_center = st.number_input("Enter temperature at the center (in degrees Celsius):", value=100.0, min_value=0.1)
temperature_edge = st.number_input("Enter temperature at the edge (in degrees Celsius):", value=20.0, min_value=0.1)


# Calculate piston head thickness using the heat transfer formula
thickness_heat_transfer = calculate_thickness_heat_transfer(H, K, temperature_center, temperature_edge)

# Display the result
st.write(f"Piston Head Thickness Based on Heat Transfer Formula: {thickness_heat_transfer:.2f} mm")
