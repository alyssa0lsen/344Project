import pandas as pd
import matplotlib.pyplot as plt

# STRUCTURAL GEOMETRY MESH CONVERGENCE
# structural 30mm
structuralGeomDF = pd.read_csv('strucural geometry mesh 3.csv')
structuralDeformation = structuralGeomDF['P2 - Total Deformation Maximum [mm]']
structuralStress = structuralGeomDF['P4 - Equivalent Stress Maximum [MPa]']
structuralSF = structuralGeomDF['P5 - Safety Factor Minimum']
numberOfElements = structuralGeomDF['P8 - Mesh Elements']
numberOfNodes = structuralGeomDF['P7 - Mesh Nodes']

marker_colours = ['#1b96c6'] * len(numberOfNodes)

# Set a specific marker style for a data point (e.g., 's' for a star) - for the 3rd point (index 2)
highlight_index = 1
marker_colours[highlight_index] = '#ef767a'

plt.plot(numberOfNodes, structuralDeformation, linestyle='-', color='#1b96c6', label='Lift/drag')

# Plot the data with customized marker styles
for x, y, colour in zip(numberOfNodes, structuralDeformation, marker_colours):
    plt.plot(x, y, marker='o', linestyle='-', color=colour, label='Lift/drag')

# plt.plot(numberOfElements, structuralDeformation, marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Number of Nodes')
plt.ylabel('Total Deformation Maximum (mm)')
plt.title('Mesh convergence - structural geometry')
plt.savefig('StructuralMeshConvergence.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the graph