# calculating the value of a given polynomial
def calc(A, x):
	return sum([ai * x**i for (i, ai) in enumerate(A)])

# calculating the value of the differential of a given polynomial
def diff(A, x):
	return sum([ai * i * x**(i-1) for (i, ai) in enumerate(A) if i != 0])
