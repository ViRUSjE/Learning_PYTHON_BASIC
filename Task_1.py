"These are variables to use in function"
name = "Milosz"
surname = "Kraska"
SENTENCE = "I want to become a programmer and work in your company, that's why I'm creating this portfolio in PyCharm by myself."
WISHES = "Have a nice day"


"""This function says hello, name and surname"""
def say_hello(a, b, c, d):
    print(f' Hi, I am {a} {b}. {c} \n {d}!')


if __name__ == '__main__':
    say_hello(name, surname, sentence, wishes)