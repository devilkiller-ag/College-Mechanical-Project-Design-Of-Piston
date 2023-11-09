import streamlit as st
import math

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

# Function to calculate piston head thickness based on the provided heat transfer formula
def calculate_thickness_heat_transfer(H, K, temperature_center, temperature_edge):
    thickness = H / (12.56 * K * (temperature_center - temperature_edge))
    return thickness

# Function to calculate piston head thickness based on the provided formula
def calculate_thickness_formula(pressure, diameter, tensile_stress):
    thickness = math.sqrt(3 * pressure * diameter**2 / (16 * tensile_stress))
    return thickness

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
st.title("Design of Piston")

# Get user input for piston diameter, pressure, tensile stress, and the number of rings with default values > 0
piston_diameter = st.number_input("Enter piston diameter (in mm):", value=100.0, min_value=0.1)
pressure_ring = st.number_input("Enter pressure on the piston ring (in N/mm^2):", value=1.0, min_value=0.1)
tensile_stress = st.number_input("Enter tensile stress (in N/mm^2):", value=10.0, min_value=0.1)
number_of_rings = st.number_input("Enter the number of rings:", value=2, min_value=1, step=1)
# pressure_load = st.number_input("Enter pressure on the piston (in N/mm^2):", value=1.0, min_value=0.1)
pressure_head = st.number_input("Enter pressure on the piston head (in N/mm^2):", value=1.0, min_value=0.1)
piston_ring_thickness = st.number_input("Enter piston ring thickness (t1) (in mm):", value=5.0, min_value=0.1)
t3 = st.number_input("Enter the initial piston wall thickness (t3) (in mm):", value=11.0, min_value=0.1)
# Get user input for H, K, temperature at the center, and temperature at the edge with default values > 0
H = st.number_input("Enter H (heat transfer coefficient):", value=1.0, min_value=0.1)
K = st.number_input("Enter K (thermal conductivity of the material):", value=1.0, min_value=0.1)
temperature_center = st.number_input("Enter temperature at the center (in degrees Celsius):", value=100.0, min_value=0.1)
temperature_edge = st.number_input("Enter temperature at the edge (in degrees Celsius):", value=20.0, min_value=0.1)

# Calculate piston head thickness using the heat transfer formula
thickness_heat_transfer = calculate_thickness_heat_transfer(H, K, temperature_center, temperature_edge)
# Calculate piston barrel dimensions and updated piston wall thickness
barrel_thickness = calculate_barrel_thickness(piston_diameter, piston_ring_thickness)
radial_depth_piston_rings = calculate_radial_depth_piston_rings(piston_ring_thickness)
updated_piston_wall_thickness = calculate_updated_piston_wall_thickness(t3)
# Calculate piston head thickness using the formula
thickness_formula = calculate_thickness_formula(pressure_head, piston_diameter, tensile_stress)
# Calculate the maximum gas load, maximum side thrust, and piston skirt length
maximum_gas_load = calculate_maximum_gas_load(piston_diameter, pressure_head)
maximum_side_thrust = calculate_maximum_side_thrust(maximum_gas_load)
piston_skirt_length = calculate_piston_skirt_length(piston_diameter)
# Calculate piston ring dimensions
radial_thickness = calculate_radial_thickness(piston_diameter, pressure_ring, tensile_stress)
max_axial_thickness = calculate_max_axial_thickness(piston_diameter, number_of_rings)
top_land_width = calculate_top_land_width(radial_thickness)
other_land_width = calculate_other_land_width(radial_thickness)

# Display the result
# st.write(f"Piston Head Thickness Based on Heat Transfer Formula: {thickness_heat_transfer:.2f} mm")
st.write(f"Thickness of the Piston Barrel: {barrel_thickness:.2f} mm")
st.write(f"Radial Depth of Piston Rings (b): {radial_depth_piston_rings:.2f} mm")
st.write(f"Updated Piston Wall Thickness (t4): {updated_piston_wall_thickness:.2f} mm")
st.write(f"Piston Head Thickness Based on the Provided Formula: {thickness_formula:.2f} mm")
st.write(f"Maximum Gas Load on the Piston (P): {maximum_gas_load:.2f} N")
st.write(f"Maximum Side Thrust on the Cylinder (R): {maximum_side_thrust:.2f} N")
st.write(f"Length of the Piston Skirt (l): {piston_skirt_length:.2f} mm")
st.write(f"Radial Thickness of the Piston Ring: {radial_thickness:.2f} mm")
st.write(f"Maximum Axial Thickness of the Piston Ring: {max_axial_thickness:.2f} mm")
st.write(f"Width of the Top Land of the Piston Ring: {top_land_width:.2f} mm")
st.write(f"Width of the Other Lands of the Piston Ring: {other_land_width:.2f} mm")