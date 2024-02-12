"Retrieving data from user"

"Function retrieves name from user and return it"
def input_name():
    name = input("Enter your name: ")
    return name
"Function retrieves last name from user and return it"
def input_last_name():
    last_name = input("Enter your last name: ")
    return last_name
"Function retrieves age from user and return it"
def input_age():
    age = (input("Enter your age: "))
    return age
"Function prints retrieved data from user"
def print_data_from_user(name, last_name, age):
    print(f"Hello {name} {last_name} you are {age} years old")

name = input_name()
last_name = input_last_name()
age = input_age()
print_data_from_user(name, last_name, age)