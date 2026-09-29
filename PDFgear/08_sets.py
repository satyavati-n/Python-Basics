# SETS IN PYTHON

# A set stores unique values.

numbers = {1, 2, 3, 4}

print(numbers)


# Duplicate values are automatically removed

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)


# Adding an element

numbers.add(5)

print(numbers)


# Removing an element

numbers.remove(2)

print(numbers)


# Set operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


# Union

print("Union:", A | B)


# Intersection

print("Intersection:", A & B)


# Difference

print("Difference:", A - B)


# Check membership

print(3 in A)
print(10 in A)