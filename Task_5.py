"Addition"

a = 128
b = 145.65
result = a + b
c = type(a)
d = type(b)
e = type(result)

"Function check type of variable and print value"
def check_and_print():
    print(f"Variable a has value {a} and type {c}")
    print(f"Variable b has value {b} and type {d}")
    print(f"Variable c has value {result} and type {e}")

check_and_print()