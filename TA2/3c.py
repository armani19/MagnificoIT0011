first=input("Enter First name: ")
last=input("Enter Last name: ")
age=input("Enter Age: ")
contact=input("Enter Contact number: ")
course=input("Enter Course: ")

print("Reading student Info: ")
print("Last name:",last)
print("First name:",first)
print("Age:",age)
print("Contact number:",contact)
print("Last name:",course)

lines=f"Last name: {last}\nFirst name: {first}\nAge: {age}\nContact number: {contact}\nCourse: {course}\n"
path= r"C:\Users\jeremy\Downloads\TA2\students.txt"
with open(path, 'a') as f:
    f.write(lines)