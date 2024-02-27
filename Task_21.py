"Multiplication table"

print("This program multiplies your number in range from 1 to 10")

a = int(input("Enter a number: "))

for i in range(1, 11):
    b = i * a
    print(f"{i} * {a} = {b}")