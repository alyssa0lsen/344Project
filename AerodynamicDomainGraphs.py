import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
domainRightDF = pd.read_csv('DomainRight.csv')
domainLeftDF = pd.read_csv('DomainLeft.csv')
domainVerticalDF = pd.read_csv('vertical 3.csv')

# DOMAIN SIZE PLOTS
# INLET TO AIRFOIL
inletToAirfoil = domainLeftDF['inletToAirfoil']
dragCoefficient = domainLeftDF['dragCoefficient']

marker_styles = ['.'] * len(inletToAirfoil)

# Set a specific marker style for a data point (e.g., 's' for a star) - for the 3rd point (index 2)
highlight_index = 2
marker_styles[highlight_index] = '*'

plt.plot(inletToAirfoil, dragCoefficient, linestyle='-', color='#1b96c6', label='Data Line')

# Plot the data with customized marker styles
for x, y, marker in zip(inletToAirfoil, dragCoefficient, marker_styles):
    plt.plot(x, y, marker=marker, linestyle='-', color='#1b96c6', label='Data Points')

#plt.plot(inletToAirfoil, dragCoefficient,marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Distance from inlet to airfoil tip (m)')
plt.ylabel('Cd')
plt.title('Domain convergence - inlet to airfoil')

plt.show()  # Display the graph

# OUTLET TO AIRFOIL
outletToAirfoil = domainRightDF['outletToAirfoil']
dragCoefficient = domainRightDF['dragCoeff']

plt.plot(outletToAirfoil, dragCoefficient, marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Distance from outlet to airfoil tip (m)')
plt.ylabel('Cd')
plt.title('Domain convergence - outlet to airfoil')
plt.show()  # Display the graph

# VERTICAL
vertical = domainVerticalDF['P15 - Vertical [m]']
dragCoefficient = domainVerticalDF['P14 - drag-coefficient-op']

marker_styles = ['.'] * len(vertical)

# Set a specific marker style for a data point (e.g., 's' for a star) - for the 3rd point (index 2)
highlight_index = 2
marker_styles[highlight_index] = '*'

plt.plot(vertical, dragCoefficient, linestyle='-', color='#1b96c6', label='Data Line')

# Plot the data with customized marker styles
for x, y, marker in zip(vertical, dragCoefficient, marker_styles):
    plt.plot(x, y, marker=marker, linestyle='-', color='#1b96c6', label='Data Points')

#plt.plot(inletToAirfoil, dragCoefficient,marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Height of Domain (m)')
plt.ylabel('Cd')
plt.title('Domain convergence - height')
plt.show()  # Display the graph
