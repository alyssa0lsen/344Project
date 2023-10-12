import pandas as pd
import matplotlib.pyplot as plt

# PRESSURE COEFFICIENTS / ANGLES OF ATTACK
negFiveDegDF = pd.read_csv('negfivedeg.csv')
negFiveDegPos = negFiveDegDF['Position']
negFiveDegPressCoeff = negFiveDegDF['Pressure Coefficient']

zeroDegDF = pd.read_csv('zerodeg.csv')
zeroDegPos = zeroDegDF['Position']
zeroDegPressCoeff = zeroDegDF['Pressure Coefficient']

fiveDegDF = pd.read_csv('fivedeg.csv')
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
#lt.title('Pressure Coefficient at Different Angles of Attack')
plt.legend()
plt.savefig('Pressure Coefficient at Different Angles of Attack.png', dpi=300, bbox_inches='tight')

plt.show()

# LIFT & DRAG VS DEGREES
liftDragDF = pd.read_csv('forces.csv')
anglesOfAttack = liftDragDF['P16 - Angle of Attack [degree]']
liftCoeff = liftDragDF['P13 - lift-coefficient-op']
dragCoeff = liftDragDF['P14 - drag-coefficient-op']
liftDrag = liftDragDF['lift/drag']

plt.plot(anglesOfAttack, liftCoeff, marker='o', label='liftCoeff', color='#1b96c6')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('Lift Coefficient')
#plt.title('Lift Coefficient at Different Angles of Attack')

# Display the plot
plt.savefig('DragAOA.png', dpi=300, bbox_inches='tight')
plt.show()

plt.plot(anglesOfAttack, dragCoeff, marker='o', label='dragCoeff', color='#1b96c6')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('Drag Coefficient')
#plt.title('Drag Coefficient at Different Angles of Attack')

# Display the plot
plt.savefig('LiftAOA.png', dpi=300, bbox_inches='tight')
plt.show()

marker_colours = ['#1b96c6'] * len(anglesOfAttack)

# Set a specific marker style for a data point (e.g., 's' for a star) - for the 3rd point (index 2)
highlight_index = 6
marker_colours[highlight_index] = '#ef767a'

plt.plot(anglesOfAttack, liftDrag, linestyle='-', color='#1b96c6', label='Lift/drag')

# Plot the data with customized marker styles
for x, y, colour in zip(anglesOfAttack, liftDrag, marker_colours):
    plt.plot(x, y, marker='o', linestyle='-', color=colour, label='Lift/drag')

#plt.plot(anglesOfAttack, liftDrag, marker='.', label='lift/drag', color='#1b96c6')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('lift/drag')
#plt.title('Lift/drag at Different Angles of Attack')
plt.savefig('LiftDragAOA.png', dpi=300, bbox_inches='tight')


# Display the plot
plt.show()

# LIFT & DRAG VS REFERENCE DATA
referenceDF = pd.read_csv('airfoil_reference_data-1.csv')
referenceAnglesOfAttack = referenceDF['# alpha']
referenceLiftCoeff = referenceDF['Cl']
referenceDragCoeff = referenceDF['Cd']
referenceLiftDrag = referenceDF['Cl/Cd']

plt.plot(anglesOfAttack, liftCoeff, label='Lift Coefficient', marker='o', color='#1b96c6')
plt.plot(referenceAnglesOfAttack, referenceLiftCoeff, label='Reference Lift Coefficient', marker='o', color='#ef767a')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('Cl')
#plt.title('Lift Coefficient at Different Angles of Attack')
plt.legend()

plt.savefig('Lift Coefficient at Different Angles of Attack.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

plt.plot(anglesOfAttack, dragCoeff, label='Drag Coefficient', marker='o', color='#1b96c6')
plt.plot(referenceAnglesOfAttack, referenceDragCoeff, label='Reference Drag Coefficient', marker='o', color='#ef767a')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('Cd')
#plt.title('Drag Coefficient at Different Angles of Attack')
plt.legend()

plt.savefig('Drag Coefficient at Different Angles of Attack.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

plt.plot(anglesOfAttack, liftDrag, label='Lift/drag', marker='o',  color='#1b96c6')
plt.plot(referenceAnglesOfAttack, referenceLiftDrag, label='Reference Lift/drag', marker='o', color='#ef767a')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('Cl/Cd')
#plt.title('Lift/drag at Different Angles of Attack')
plt.legend()

#plt.savefig('Lift/drag at Different Angles of Attack.png', dpi=300, bbox_inches='tight')
plt.savefig('LiftDrag at Different Angles of Attack.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

# 20 degrees AOA

twentyDegDF = pd.read_csv('pressure_coefficient_20.csv')
twentyDegPos = twentyDegDF['Position']
twentyDegPressCoeff = twentyDegDF['Pressure Coefficient']

plt.plot(twentyDegPos, twentyDegPressCoeff, label='15 degrees', color='#1b96c6')

plt.xlabel('Position (m)')
plt.ylabel('Pressure Coefficient')
plt.savefig('Pressure Coefficient 20 degrees.png', dpi=300, bbox_inches='tight')

plt.show()
