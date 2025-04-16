student_details= {
    "Alice": 85,
    "John":60,
    "Peter": 71,
    "Chris": 55
}

name= input("Enter the studenten\'s name:")

if name in student_details:
    print(f"{name}\'s marks : {student_details[name]}")
else :
    print("Student not found.")