# calculating the value of a given polynomial
def calc(A, x):
	return sum([ai * x**i for (i, ai) in enumerate(A)])

# calculating the value of the differential of a given polynomial
def diff(A, x):
	return sum([ai * i * x**(i-1) for (i, ai) in enumerate(A) if i != 0])

# calculating the integral of the polynomial for a given range
def integral(A, x0, x1, n):
	dx = (float(x1) - float(x0)) / n
	return sum([calc(A, x0 + i * dx) * dx for i in range(int(n))])

# calculating the Newton Method for a given polynomial and a precission
def newtons_method(A, x, e):
	if calc(A, x) <= e:
		print "x: ", x, "f(x) = ", calc(A, x)
		return

	newtons_method(A, x - (calc(A, x) / diff(A, x)), e)
