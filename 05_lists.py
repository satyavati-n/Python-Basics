#LIST IN PYTHON 

# Creating a list

fruits = ["Apple", "Banana", "Mango"]

print(fruits)


# Accessing elements

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Negative indexing

print(fruits[-1])


# Changing an element

fruits[0] = "Orange"

print(fruits)


# Adding an element

fruits.append("Grapes")

print(fruits)


# Insert at a specific position

fruits.insert(1, "Watermelon")

print(fruits)


# Removing an element

fruits.remove("Banana")

print(fruits)


# Length of list

print("Number of fruits:", len(fruits))


# Loop through a list

for fruit in fruits:
    print(fruit)