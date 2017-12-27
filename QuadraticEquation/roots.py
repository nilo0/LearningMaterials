from math import sqrt

# ask user for coefficients
C = [input('insert coeff ' + str(i+1) + ' : ') for i in range(3)]

# Calculating delta
delta = C[1]**2 - 4 * C[0] * C[2]

_2a = 2 * C[0]

if delta >= 0:
    x1 = (-C[1] - sqrt(delta)) / _2a
    x2 = (-C[1] + sqrt(delta)) / _2a
else:
    x1 = str(-C[1] / _2a) + " + i * " + str(sqrt(-delta) / _2a)
    x2 = str(-C[1] / _2a) + " - i * " + str(sqrt(-delta) / _2a)

print(x1, x2)
