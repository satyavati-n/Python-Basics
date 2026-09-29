# FILE INPUT AND OUTPUT

# Writing to a file

file = open("example.txt", "w")

file.write("Hello, Python!\n")
file.write("This is my first file.")

file.close()


# Reading from a file

file = open("example.txt", "r")

content = file.read()

print(content)

file.close()


# Using 'with'


with open("example.txt", "w") as file:
    file.write("Python file handling is easy!")


with open("example.txt", "r") as file:
    content = file.read()

print(content)


# Appending to a file

with open("example.txt", "a") as file:
    file.write("\nThis line was added later.")


with open("example.txt", "r") as file:
    print(file.read())