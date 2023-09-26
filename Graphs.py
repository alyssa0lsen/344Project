import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
inletVelocityDF = pd.read_csv('InletVelocityVerification.csv')
pressureDF = pd.read_csv('PressureVerification.csv')
wallsPressureDF = pd.read_csv('WallsPressureVerification.csv')
wallsVelocityDF = pd.read_csv('WallsVelocityVerification.csv')
domainRightDF = pd.read_csv('DomainRight.csv')
domainLeftDF = pd.read_csv('DomainLeft.csv')

# INLET VELOCITY VERIFICATION PLOT
yVelocity = inletVelocityDF['Y']
inletVelocity = inletVelocityDF['Inlet Velocity']
outletVelocity = inletVelocityDF['Outlet Velocity']

plt.plot(yVelocity, inletVelocity, label='Inlet', color = '#1b96c6')
plt.plot(yVelocity, outletVelocity, label='Outlet',color = '#ef767a')

plt.xlabel('Y (m)')
plt.ylabel('Velocity (m/s)')
plt.title('Verification of Inlet Velocity')
plt.legend()

plt.show()  # Display the graph


# PRESSURE VERIFICATION PLOT
yPressure = pressureDF['Y [ m ]']
inletPressure = pressureDF['Inlet Pressure [ Pa ]']
outletPressure = pressureDF['Outlet Pressure [ Pa ]']

plt.plot(yPressure, inletPressure, label='Inlet', color='#1b96c6')
plt.plot(yPressure, outletPressure, label='Outlet', color='#ef767a')

plt.xlabel('Y (m)')
plt.ylabel('Pressure (Pa)')
plt.title('Verification of Pressure')
plt.legend()

plt.show()  # Display the graph


# PRESSURE AT WALLS VERIFICATION PLOT
xPressure = wallsPressureDF['X [ m ]']
pressure = wallsPressureDF['Pressure [ Pa ]']

plt.plot(xPressure, pressure, label='Inlet', color='#1b96c6')

plt.xlabel('X (m)')
plt.ylabel('Pressure (Pa)')
plt.title('Verification of Pressure at Walls')

plt.show()


# VELOCITY AT WALLS VERIFICATION PLOT
xVelocity = wallsVelocityDF['X [ m ]']
velocity = wallsVelocityDF['Velocity [ m s^-1 ]']

plt.plot(xVelocity, velocity, label='Inlet', color='#1b96c6')

plt.xlabel('X (m)')
plt.ylabel('Velocity (m/s)')
plt.title('Verification of Velocity at Walls')

plt.show()


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

plt.plot(outletToAirfoil, dragCoefficient,marker='o', label='Cd', color='#1b96c6')

plt.xlabel('Distance from outlet to airfoil tip (m)')
plt.ylabel('Cd')
plt.title('Domain convergence - outlet to airfoil')
plt.show()  # Display the graph

# VERTICAL

# STRUCTURAL GEOMETRY MESH CONVERGENCE

# PRESSURE COEFFICIENTS / ANGLES OF ATTACK
negFiveDegDF = pd.read_csv('negfivedeg.csv')
negFiveDegPos = negFiveDegDF['Position']
negFiveDegPressCoeff = negFiveDegDF['Pressure Coefficient']

zeroDegDF = pd.read_csv('zerodeg.csv')
zeroDegPos = zeroDegDF['Position']
zeroDegPressCoeff = zeroDegDF['Pressure Coefficient']

fiveDegDF = pd.read_csv('fivedeg - Copy.csv')
fiveDegPos = fiveDegDF['Position']
fiveDegPressCoeff = fiveDegDF['Pressure Coefficient']

tenDegDF = pd.read_csv('tendeg.csv')
tenDegPos = tenDegDF['Position']
tenDegPressCoeff = tenDegDF['Pressure Coefficient']

fifteenDegDF = pd.read_csv('fifteendeg.csv')
fifteenDegPos = fifteenDegDF['Position']
fifteenDegPressCoeff = fifteenDegDF['Pressure Coefficient']


plt.plot(negFiveDegPos, negFiveDegPressCoeff, label='-5 degrees', color='#1b96c6')

plt.plot(zeroDegPos, zeroDegPressCoeff, label='0 degrees', color='#ef767a')

plt.plot(fiveDegPos, fiveDegPressCoeff, label='5 degrees', color='#49dcb1')

plt.plot(tenDegPos, tenDegPressCoeff, label='10 degrees', color='#456990')

plt.plot(fifteenDegPos, fifteenDegPressCoeff, label='15 degrees', color='#eeb868')

plt.xlabel('Position (m)')
plt.ylabel('Pressure Coefficient')
plt.title('Pressure Coefficient at Different Angles of Attack')
plt.legend()

# Display the plot
#plt.grid(True)
plt.show()