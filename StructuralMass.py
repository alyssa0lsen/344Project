import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

safetyFactorDF = pd.read_csv('MassSafetyFactor.csv')
thicknessDF = pd.read_csv('MassThickness.csv')
diameterDF = pd.read_csv('MassDiameter.csv')

thickness = thicknessDF['P10 - InwardThickness [m]']
tMass = thicknessDF['P8 - Solid Mass [kg]']

diameter = diameterDF['P9 - Diameter [m]']
dMass = diameterDF['P8 - Solid Mass [kg]']

safetyFactor = safetyFactorDF['P5 - Safety Factor Minimum']
sMass = safetyFactorDF['P8 - Solid Mass [kg]']

# Thickness vs Mass
plt.plot(thickness, tMass, marker='o', label='Cd', color='#1b96c6')
plt.xlabel('Thickness (m)')
plt.ylabel('Mass (kg)')
plt.savefig('SparThicknessToMass.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the graph

# Diameter vs Mass
plt.plot(diameter, dMass, marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Diameter (m)')
plt.ylabel('Mass (kg)')
plt.savefig('SparDiameterToMass.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the graph

# Mass vs Safety Factor
plt.plot(sMass, safetyFactor, marker='o', label='Cd', color='#1b96c6')
plt.axhline(1.5, color='#ef767a', linestyle='--', label='Horizontal Line at Safety Factor = 1.5')

plt.xlabel('Mass (kg)')
plt.ylabel('Safety Factor')
plt.savefig('SparMassToSafetyFactor.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the graph
