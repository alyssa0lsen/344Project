import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# AERODYNAMIC GEOMETRY MESH CONVERGENCE
# 20mm
#aerodynamicGeomDF = pd.read_csv('aerodynamic mesh with 10,14,10.csv')
aerodynamicGeomDF = pd.read_csv('final geometric mesh convergence.csv')

dragCoefficient = aerodynamicGeomDF['P14 - drag-coefficient-op']
numberOfElements = aerodynamicGeomDF['P7 - Mesh Elements']
numberOfNodes = aerodynamicGeomDF['P24 - Mesh Nodes']
sqrtNumElements = 1/np.sqrt(numberOfElements)

plt.plot(numberOfNodes, dragCoefficient, marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Number of Nodes')
plt.ylabel('Cd')
plt.title('Mesh convergence - aerodynamic geometry')
plt.show()  # Display the graph