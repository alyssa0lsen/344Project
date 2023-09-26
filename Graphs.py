import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
inletVelocityDF = pd.read_csv('InletVelocityVerification.csv')
pressureDF = pd.read_csv('PressureVerification.csv')
wallsPressureDF = pd.read_csv('WallsPressureVerification.csv')
wallsVelocityDF = pd.read_csv('WallsVelocityVerification.csv')


# Create a line plot
yVelocity = inletVelocityDF['Y']
inletVelocity = inletVelocityDF['Inlet Velocity']
outletVelocity = inletVelocityDF['Outlet Velocity']

plt.plot(yVelocity, inletVelocity, label='Inlet', color = '#1b96c6')
plt.plot(yVelocity, outletVelocity, label='Outlet',color = '#ef767a')


# Customize the graph
plt.xlabel('Y (m)')
plt.ylabel('Velocity (m/s)')
plt.title('Verification of Inlet Velocity')
plt.legend()

# Display or save the graph
plt.show()  # Display the graph
# plt.savefig('output_graph.png')  # Save the graph to a file

# Create a line plot
yPressure = pressureDF['Y [ m ]']
inletPressure = pressureDF['Inlet Pressure [ Pa ]']
outletPressure = pressureDF['Outlet Pressure [ Pa ]']

plt.plot(yPressure, inletPressure, label='Inlet', color='#1b96c6')
plt.plot(yPressure, outletPressure, label='Outlet', color='#ef767a')


# Customize the graph
plt.xlabel('Y (m)')
plt.ylabel('Pressure (Pa)')
plt.title('Verification of Pressure')
plt.legend()

# Display or save the graph
plt.show()  # Display the graph
# plt.savefig('output_graph.png')  # Save the graph to a file

# Create a line plot
xPressure = wallsPressureDF['X [ m ]']
pressure = wallsPressureDF['Pressure [ Pa ]']

plt.plot(xPressure, pressure, label='Inlet', color='#1b96c6')


# Customize the graph
plt.xlabel('X (m)')
plt.ylabel('Pressure (Pa)')
plt.title('Verification of Pressure at Walls')

# Display or save the graph
plt.show()  # Display the graph
# plt.savefig('output_graph.png')  # Save the graph to a file

# Create a line plot
xVelocity = wallsVelocityDF['X [ m ]']
velocity = wallsVelocityDF['Velocity [ m s^-1 ]']

plt.plot(xVelocity, velocity, label='Inlet', color='#1b96c6')


# Customize the graph
plt.xlabel('X (m)')
plt.ylabel('Velocity (m/s)')
plt.title('Verification of Velocity at Walls')

# Display or save the graph
plt.show()  # Display the graph
# plt.savefig('output_graph.png')  # Save the graph to a file