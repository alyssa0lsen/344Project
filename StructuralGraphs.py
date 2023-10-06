import pandas as pd
import matplotlib.pyplot as plt

# STRUCTURAL GEOMETRY MESH CONVERGENCE
# structural 30mm
structuralGeomDF = pd.read_csv('strucural geometry mesh 3.csv')
structuralDeformation = structuralGeomDF['P2 - Total Deformation Maximum [mm]']
structuralStress = structuralGeomDF['P4 - Equivalent Stress Maximum [MPa]']
structuralSF = structuralGeomDF['P5 - Safety Factor Minimum']
numberOfElements = structuralGeomDF['P8 - Mesh Elements']

plt.plot(numberOfElements, structuralDeformation, marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Number of Elements')
plt.ylabel('Total Deformation Maximum (mm)')
plt.title('Mesh convergence - structural geometry')
plt.show()  # Display the graph