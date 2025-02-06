path = r"C:\Users\jeremy\Downloads\TA2\students.txt"

with open(path, 'r') as f:
    contents=f.read()

print("Reading Student Information:")
print(contents)