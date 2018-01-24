from lib import quadratic_equation as qe

# ask user for coefficients
C = [input('insert coeff ' + str(i+1) + ' : ') for i in range(3)]

x1, x2 = qe.roots(C[0], C[1], C[2])

print(x1, x2)
