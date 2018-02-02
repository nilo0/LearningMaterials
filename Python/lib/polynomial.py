class Polynomial:
	def __init__(self, A):
		self.A = A

	def calc(self, x):
		return sum([ai * x**i for (i, ai) in enumerate(self.A)])

	def diff(self, x):
		return sum([ai * i * x**(i-1) for (i, ai) in enumerate(self.A) if i != 0])

	def integral(self, x0, x1, n):
		dx = (float(x1) - float(x0)) / n
		return sum([self.calc(x0 + i * dx) * dx for i in range(int(n))])

	def newtons_method(self, x, e):
		if self.calc(x) <= e:
			print "x: ", x, "f(x) = ", self.calc(x)
			return

		self.newtons_method(x - (self.calc(x) / self.diff(x)), e)
