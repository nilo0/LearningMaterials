from lib import polynomial as poly

# reading input from user
print('Please enter coeff tuple: ')
coeff = tuple(float(x.strip()) for x in raw_input().split(','))
x0 = float(input('Please enter x0: '))
E = float(input('Please enter e: '))

# calling newton fct with user's inputs
poly.newtons_method(coeff, x0, E)
