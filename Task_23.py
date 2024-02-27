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

if summary > average:
    print("The sum is greater!")
elif summary == average:
    print("sum = average")
else:
    print("The average is greater")

print(f"Sum: {summary}")
print(f"Average: {average}")
