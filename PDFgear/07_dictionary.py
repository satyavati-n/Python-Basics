# PYTHON DICTIONARIES


# Dictionary stores data as key-value pairs.

student = {
    "name": "Satyavati",
    "age": 17,
    "marks": 95
}

print(student)


# Accessing values

print(student["name"])
print(student["age"])
print(student["marks"])


# Adding a new key-value pair

student["city"] = "Bangalore"

print(student)


# Changing a value

student["marks"] = 98

print(student)


# Removing a value

student.pop("city")

print(student)


# Getting keys

print(student.keys())


# Getting values

print(student.values())


# Getting key-value pairs

print(student.items())


# Loop through dictionary

for key, value in student.items():
    print(key, ":", value)