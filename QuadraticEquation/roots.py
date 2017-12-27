# ask user for a triple
a = input("Please insert coefficient a: ")
b = input("Please insert coefficient b: ")
c = input("please insert coefficient c: ")

# Calculating delta
delta = b**2 - 4*a*c
if delta > 0:
    x_1 = (-b - sqrt(delt)) / 2*a
    x_2 = (-b + sqrt(delt)) / 2*a
    print(x_1, x_2)

if delta == 0:
    x = -b / (2*a)
    print(x)

if delta < 0:
    print(":D nadarim agha")
