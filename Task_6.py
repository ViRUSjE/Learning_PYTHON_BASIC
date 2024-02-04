"Mathematical operations"

"Variables for task"
a = 25
b = 10

print(f"Variable a has value {a}")
print(f"Variable b has value {b}")

"Function returns addition value of two variables"
def sum_of_variables(a, b):
    return a + b

"Function substract two variables"
def subtract_variables(a, b):
    return a - b

"Function returns multiplication value of two variables"
def multiply_variables(a, b):
    c = a * b
    return c

"Funtcion returns division value of two variables"
def divide_variables(a, b):
    c = a / b
    return c

"Function returns modulo value of two variables"
def modulo_variables(a, b):
    c = a % b
    return c

"Function returns division value of two variables"
def devide_variables_int(a, b):
    c = a // b
    return c

"Printing all functions"
print(f"Addition value", sum_of_variables(a, b))
print(f"Subtraction value", subtract_variables(a, b))
print(f"Multiplication value", multiply_variables(a, b))
print(f"Division value", divide_variables(a, b))
print(f"Modulo value", modulo_variables(a, b))
print(f"Integer division value", devide_variables_int(a, b))
