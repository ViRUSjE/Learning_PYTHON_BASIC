"User's age"
import datetime

cur_datatime = datetime.datetime.now()

user_name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
cur_year = cur_datatime.year
age = cur_year - birth_year

print(f"User: {user_name} is {age} years old")
