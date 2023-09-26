import pandas as pd
import matplotlib.pyplot as plt

# AERODYNAMIC GEOMETRY MESH CONVERGENCE
aerodynamicGeomDF = pd.read_csv('aerodynamic mesh with 10,14,10.csv')
dragCoefficient = aerodynamicGeomDF['P14 - drag-coefficient-op']
numberOfElements = aerodynamicGeomDF['P7 - Mesh Elements']

plt.plot(numberOfElements, dragCoefficient, marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Number of Elements')
plt.ylabel('Cd')
plt.title('Mesh convergence - aerodynamic geometry')
plt.show()  # Display the graph