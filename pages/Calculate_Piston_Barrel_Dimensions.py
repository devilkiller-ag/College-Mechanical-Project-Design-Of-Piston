import streamlit as st

# Function to calculate the thickness of the piston barrel
def calculate_barrel_thickness(diameter, piston_ring_thickness):
    thickness = 0.03 * diameter + piston_ring_thickness + 4.5
    return thickness

# Function to calculate the radial depth of the piston rings (b)
def calculate_radial_depth_piston_rings(piston_ring_thickness):
    b = piston_ring_thickness + 0.4
    return b

# Function to calculate the updated thickness of the piston wall (t4)
def calculate_updated_piston_wall_thickness(t3):
    t4 = 0.35 * t3
    return t4

# Create a Streamlit app
st.title("Piston Barrel Dimensions Calculator")

# Get user input for piston diameter, piston ring thickness (t1), and initial piston wall thickness (t3) with default values > 0
piston_diameter = st.number_input("Enter piston diameter (in mm):", value=100.0, min_value=0.1)
piston_ring_thickness = st.number_input("Enter piston ring thickness (t1) (in mm):", value=5.0, min_value=0.1)
t3 = st.number_input("Enter the initial piston wall thickness (t3) (in mm):", value=10.0, min_value=0.1)

# Calculate piston barrel dimensions and updated piston wall thickness
barrel_thickness = calculate_barrel_thickness(piston_diameter, piston_ring_thickness)
radial_depth_piston_rings = calculate_radial_depth_piston_rings(piston_ring_thickness)
updated_piston_wall_thickness = calculate_updated_piston_wall_thickness(t3)

# Display the results
st.write(f"Thickness of the Piston Barrel: {barrel_thickness:.2f} mm")
st.write(f"Radial Depth of Piston Rings (b): {radial_depth_piston_rings:.2f} mm")
st.write(f"Updated Piston Wall Thickness (t4): {updated_piston_wall_thickness:.2f} mm")
