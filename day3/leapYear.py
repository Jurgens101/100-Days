#ask user for a year
userYear = int(input("Enter a year to check if its leap or not: "))

if (userYear % 4 == 0 and userYear % 100 != 0 or userYear % 400 == 0):
    print(f"{userYear} is a leap year! ")
else:
    print(f"{userYear} is not a leap year! ")