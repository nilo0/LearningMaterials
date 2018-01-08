from MyModules import polynomial as poly

# calculating the Newton Method for a given polynomial and a precission
def newton(A, x, e):
	if poly.calc(A, x) <= e:
		print "x: ", x, "f(x) = ", poly.calc(A, x)
		return

	newton(A, x - (poly.calc(A, x) / poly.diff(A, x)), e)


# reading input from user
print('Please enter coeff tuple: ')
coeff = tuple(float(x.strip()) for x in raw_input().split(','))
x0 = float(input('Please enter x0: '))
E = float(input('Please enter e: '))

# calling newton fct with user's inputs
newton(coeff, x0, E)
