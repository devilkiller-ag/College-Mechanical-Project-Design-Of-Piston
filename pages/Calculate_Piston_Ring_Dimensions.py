import streamlit as st
import math

# Function to calculate radial thickness of the piston ring
def calculate_radial_thickness(diameter, pressure, tensile_stress):
    thickness = diameter * math.sqrt(3 * pressure / tensile_stress)
    return thickness

# Function to calculate the maximum axial thickness of the piston ring
def calculate_max_axial_thickness(diameter, number_of_rings):
    thickness = diameter / 10 * number_of_rings
    return thickness

# Function to calculate the width of the top land of the piston ring
def calculate_top_land_width(piston_head_thickness):
    width = piston_head_thickness * 1.2
    return width

# Function to calculate the width of the other lands of the piston ring
def calculate_other_land_width(thickness):
    width = 0.75 * thickness
    return width

# Create a Streamlit app
st.title("Piston Ring Dimensions Calculator")

# Get user input for piston diameter, pressure, tensile stress, and the number of rings with default values > 0
piston_diameter = st.number_input("Enter piston diameter (in mm):", value=100.0, min_value=0.1)
pressure = st.number_input("Enter pressure on the piston ring (in N/mm^2):", value=1.0, min_value=0.1)
tensile_stress = st.number_input("Enter tensile stress (in N/mm^2):", value=10.0, min_value=0.1)
number_of_rings = st.number_input("Enter the number of rings:", value=2, min_value=1, step=1)

# Calculate piston ring dimensions
radial_thickness = calculate_radial_thickness(piston_diameter, pressure, tensile_stress)
max_axial_thickness = calculate_max_axial_thickness(piston_diameter, number_of_rings)
top_land_width = calculate_top_land_width(radial_thickness)
other_land_width = calculate_other_land_width(radial_thickness)

# Display the results
st.write(f"Radial Thickness of the Piston Ring: {radial_thickness:.2f} mm")
st.write(f"Maximum Axial Thickness of the Piston Ring: {max_axial_thickness:.2f} mm")
st.write(f"Width of the Top Land of the Piston Ring: {top_land_width:.2f} mm")
st.write(f"Width of the Other Lands of the Piston Ring: {other_land_width:.2f} mm")
