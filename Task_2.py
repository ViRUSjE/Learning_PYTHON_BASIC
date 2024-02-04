"Data types"
a = 2
b = 6
colour = 0xf200b5
c = 2.5
d = b / a
sqrt_minus_four = 2j
binary = 0b1101
bank_balance = -177.58

"Function check type of variable"
def check_type(data):
    result = type(data)
    print(f"Checking of type variable {data}" )
    print(f"Type of {data} is {result}")

if __name__ == '__main__':
    check_type(a)
    check_type(c)
    check_type(d)
    check_type(colour)
    check_type(sqrt_minus_four)
    check_type(bank_balance)
    check_type(binary)