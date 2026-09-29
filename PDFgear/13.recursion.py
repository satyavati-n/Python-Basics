# PYTHON RECURSION


# Recursion means a function calls itself.


# Simple recursion example

def countdown(n):

    # Base condition
    if n == 0:
        print("Done!")
        return

    print(n)

    # Function calling itself
    countdown(n - 1)


countdown(5)


# Factorial using recursion

def factorial(n):

    # Base case
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)


print("Factorial:", factorial(5))