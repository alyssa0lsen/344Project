import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
domainRightDF = pd.read_csv('DomainRight.csv')
domainLeftDF = pd.read_csv('DomainLeft.csv')
domainVerticalDF = pd.read_csv('vertical 3.csv')

# DOMAIN SIZE PLOTS
# 10 left to airfoil, 14 right to airfoil and 10 height
# INLET TO AIRFOIL
inletToAirfoil = domainLeftDF['inletToAirfoil']
dragCoefficient = domainLeftDF['dragCoefficient']

marker_colours = ['#1b96c6'] * len(inletToAirfoil)

# Set a specific marker style for a data point (e.g., 's' for a star) - for the 3rd point (index 2)
highlight_index = 2
marker_colours[highlight_index] = '#ef767a'

plt.plot(inletToAirfoil, dragCoefficient, linestyle='-', color='#1b96c6', label='Data Line')

# Plot the data with customized marker styles
for x, y, colour in zip(inletToAirfoil, dragCoefficient, marker_colours):
    plt.plot(x, y, marker='o', linestyle='-', color=colour, label='Data Points')

#plt.plot(inletToAirfoil, dragCoefficient,marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Distance from inlet to airfoil tip (m)')
plt.ylabel('Cd')
#plt.title('Domain convergence - inlet to airfoil')
plt.savefig('DomainAirfoilToInletConvergence.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the graph

# OUTLET TO AIRFOIL
outletToAirfoil = domainRightDF['outletToAirfoil']
dragCoefficient = domainRightDF['dragCoeff']

marker_colours = ['#1b96c6'] * len(outletToAirfoil)

# Set a specific marker style for a data point (e.g., 's' for a star) - for the 3rd point (index 2)
highlight_index = 1
marker_colours[highlight_index] = '#ef767a'

plt.plot(outletToAirfoil, dragCoefficient, linestyle='-', color='#1b96c6', label='Data Line')

# Plot the data with customized marker styles
for x, y, colour in zip(outletToAirfoil, dragCoefficient, marker_colours):
    plt.plot(x, y, marker='o', linestyle='-', color=colour, label='Data Points')

plt.xlabel('Distance from outlet to airfoil tip (m)')
plt.ylabel('Cd')
#plt.title('Domain convergence - outlet to airfoil')
plt.savefig('DomainAirfoilToOutletConvergence.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the graph

# VERTICAL
vertical = domainVerticalDF['P15 - Vertical [m]']
dragCoefficient = domainVerticalDF['P14 - drag-coefficient-op']

marker_colours = ['#1b96c6'] * len(vertical)

# Set a specific marker style for a data point (e.g., 's' for a star) - for the 3rd point (index 2)
highlight_index = 9
marker_colours[highlight_index] = '#ef767a'

plt.plot(vertical, dragCoefficient, linestyle='-', color='#1b96c6', label='Data Line')

# Plot the data with customized marker styles
for x, y, colour in zip(vertical, dragCoefficient, marker_colours):
    plt.plot(x, y, marker='o', linestyle='-', color=colour, label='Data Points')

#plt.plot(inletToAirfoil, dragCoefficient,marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Height of Domain (m)')
plt.ylabel('Cd')
#plt.title('Domain convergence - height')
plt.savefig('DomainHeightConvergence.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the graph
