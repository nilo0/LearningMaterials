# ask user for a triple
coeffs = [input('insert coeff ' + str(i+1) + ' : ') for i in range(3)]

# Calculating delta
delta = coeffs[1]**2 - 4 * coeffs[0] * coeffs[2]

if delta > 0:
    x_1 = (-coeffs[1] - sqrt(delt)) / (2 * coeffs[0])
    x_2 = (-coeffs[1] + sqrt(delt)) / (2 * coeffs[0])
    print(x_1, x_2)
elif delta == 0:
    x = -coeffs[1] / (2*coeffs[0])
    print(x)
else:
    print(":D nadarim agha")
