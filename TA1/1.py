var=input("Enter the string: ")

vowelss=0
vowels="AEIOUaeiou"
consonant=0
space=0
characters=0

for char in var:
    if char in vowels:
        vowelss+=1
    elif char.isalpha():
        consonant+=1
    elif char.isspace():
        space+=1
    else:
        characters=+1

print("vowels:", vowelss)
print("consonant:", consonant)
print("space:", space)
print("other characters:", characters)