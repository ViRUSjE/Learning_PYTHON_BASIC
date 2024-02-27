"Quadratic equation"
import cmath

print("Equation: a*x**2 + b*x + c == 0")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x_1 = (-b - cmath.sqrt(delta)) / (2*a)
    x_2 = (-b + cmath.sqrt(delta))/ (2*a)
    print(f"Result: X1 = {x_1}, X2 = {x_2}")
elif delta == 0:
    print("Delta = 0 \n x_1 = x_2")
else:
    print("Delta <0 there is no solution in the set of real numbers")
