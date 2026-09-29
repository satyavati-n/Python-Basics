# IF, ELIF AND ELSE


age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")



# if - elif - else


marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Needs improvement")



# Nested if


age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")