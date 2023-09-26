import pandas as pd
import matplotlib.pyplot as plt

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

plt.show()

# LIFT / DRAG VS DEGREES
liftDragDF = pd.read_csv('forces.csv')
anglesOfAttack = liftDragDF['P16 - Angle of Attack [degree]']
liftCoeff = liftDragDF['P13 - lift-coefficient-op']
dragCoeff = liftDragDF['P14 - drag-coefficient-op']
liftDrag = liftDragDF['lift/drag']

plt.plot(anglesOfAttack, liftCoeff, marker='.', label='liftCoeff', color='#1b96c6')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('Lift Coefficient')
plt.title('Lift Coefficient at Different Angles of Attack')

# Display the plot
plt.show()

plt.plot(anglesOfAttack, dragCoeff, marker='.', label='dragCoeff', color='#1b96c6')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('Drag Coefficient')
plt.title('Drag Coefficient at Different Angles of Attack')

# Display the plot
plt.show()

plt.plot(anglesOfAttack, liftDrag, marker='.', label='lift/drag', color='#1b96c6')

plt.xlabel('Angle of Attack (degree)')
plt.ylabel('lift/drag')
plt.title('Lift/drag at Different Angles of Attack')

# Display the plot
plt.show()