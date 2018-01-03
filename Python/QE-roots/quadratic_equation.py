from cmath import sqrt

def delta(a, b, c):
    return b**2 - (4 * a * c)

def roots(a, b, c):
    d = delta(a, b, c)

    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a) + 1j * 0
        x2 = (-b - sqrt(d)) / (2 * a) + 1j * 0
    else:
        x1 = -b / (2 * a) + 1j * sqrt(-d) / (2 * a)
        x2 = -b / (2 * a) - 1j * sqrt(-d) / (2 * a)

    return x1, x2
