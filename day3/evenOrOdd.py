#ask user for a number
userNumber = int(input("Enter a number to check if it's even or odd: "))

if userNumber % 2 == 0:
    print(f"{userNumber} is even! ")
else:
    print(f"{userNumber} is odd! ")
    