# FUNCTIONS IN PYTHON

# Creating a function

def greet():
    print("Hello, welcome to Python!")


# Calling the function

greet()


# Function with parameters


def greet_user(name):
    print("Hello", name)


greet_user("Satyavati")
greet_user("Vaishnavi")

# Function with multiple parameters


def add(a, b):
    print("Sum:", a + b)


add(10, 20)


# Function with return


def multiply(a, b):
    return a * b


result = multiply(5, 4)

print("Result:", result)


# Default parameter


def welcome(name="Student"):
    print("Welcome", name)


welcome()
welcome("Satyavati")