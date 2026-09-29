# RANGE()

# range(stop)

for i in range(5):
    print(i)


# range(start, stop)

for i in range(2, 6):
    print(i)


# range(start, stop, step)

for i in range(1, 10, 2):
    print(i)


# Counting backwards

for i in range(10, 0, -1):
    print(i)


# Creating a range and converting it to a list

numbers = list(range(1, 6))

print(numbers)


# Practical example

for number in range(1, 11):
    print("Number:", number)