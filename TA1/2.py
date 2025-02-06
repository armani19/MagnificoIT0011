sum=0

string=input("Enter string digits: ")
for char in string:
    if char.isdigit():
        sum+=int(char)

print("Sum: "+str(sum))