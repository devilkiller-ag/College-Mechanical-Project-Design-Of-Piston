import streamlit as st

# Function to calculate the maximum gas load on the piston (P)
def calculate_maximum_gas_load(diameter, pressure):
    P = pressure * (3.14 * diameter**2 / 4)
    return P

# Function to calculate the maximum side thrust on the cylinder (R)
def calculate_maximum_side_thrust(P):
    R = 1/10 * P
    return R

# Function to calculate the length of the piston skirt (l)
def calculate_piston_skirt_length(diameter, lower_limit=0.65, upper_limit=0.8):
    l = diameter * (lower_limit + upper_limit) / 2
    return l

# Create a Streamlit app
st.title("Piston Load and Skirt Length Calculator")

# Get user input for piston diameter and pressure with default values > 0
piston_diameter = st.number_input("Enter piston diameter (in mm):", value=100.0, min_value=0.1)
pressure = st.number_input("Enter pressure on the piston (in N/mm^2):", value=1.0, min_value=0.1)

# Calculate the maximum gas load, maximum side thrust, and piston skirt length
maximum_gas_load = calculate_maximum_gas_load(piston_diameter, pressure)
maximum_side_thrust = calculate_maximum_side_thrust(maximum_gas_load)
piston_skirt_length = calculate_piston_skirt_length(piston_diameter)

# Display the results
st.write(f"Maximum Gas Load on the Piston (P): {maximum_gas_load:.2f} N")
st.write(f"Maximum Side Thrust on the Cylinder (R): {maximum_side_thrust:.2f} N")
st.write(f"Length of the Piston Skirt (l): {piston_skirt_length:.2f} mm")
