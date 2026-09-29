# LOOPS IN PYTHON

# FOR LOOP


for i in range(5):
    print(i)


# Loop through a list

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# WHILE LOOP


count = 1

while count <= 5:
    print(count)
    count += 1


# BREAK

for i in range(10):

    if i == 5:
        break

    print(i)


# CONTINUE

for i in range(10):

    if i == 5:
        continue

    print(i)