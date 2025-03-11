def classify_age():
    Age = int(input("How much is your age:"))
    
    if Age < 0:
        print("Invalid input, try again.")
    elif Age < 13:
        print("You're a child.")
    elif Age < 20:
        print("You're a teenager.")
    elif Age < 65:
        print("You're an adult.")
    else:
        print("You're a senior.")
    
classify_age()
