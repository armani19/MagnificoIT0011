while True:
    print("Menu:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")
    
    choice = input("Enter your choice: ").upper()
    
    if choice in ["D", "E", "R", "F"]:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
            
        if choice == "D":
            if b == 0:
                    print("invalid")
            else:
                    print("Result:", a / b)
            
        elif choice == "E":
            print("Result:", a ** b)
            
        elif choice == "R":
            if b == 0:
                    print("Invalid")
            else:
                    print("Result:", a % b)
            
        elif choice == "F":
            if b <= a:
                    print("Invalid")
            else:
                    print("Result:", sum(range(a, b + 1)))
    else:
        print("Invalid choice")