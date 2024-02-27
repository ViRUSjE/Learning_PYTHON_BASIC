"Average"

"This program calculates the average of n numbers from provided by user"

numbers = []

a = int(input("Enter n: "))

for i in range(a):
    b = input("Enter number: ")
    numbers.append(b)

print(f"Your numbers: {numbers}")

summary = 0

for nu in numbers:
    summary += float(nu)

average = summary / a

print(f"Result: {average}")