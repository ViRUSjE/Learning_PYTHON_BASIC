"Sum of numbers"

print("This program sums all numbers from 0 up to n")

n = int(input("Enter n: "))

result = 0

for i in range(n+1):
    result += i

print(result)

