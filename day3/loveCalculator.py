#ask the user to enter 2 names to see if they match
print("Hello, please enter 2 names to check if they are a match!")
nameOne = input("Enter the first name: \n") 
nameTwo = input("Enter the second name:\n")

#adding the 2 names together
matchingName = nameOne + nameTwo

#turning names to lowercase
matchingName = matchingName.lower()

#counting the total of each letter in the string
t = matchingName.count('t')
r = matchingName.count('r')
u = matchingName.count('u')
e = matchingName.count('e')
l = matchingName.count('l')
o = matchingName.count('o')
v = matchingName.count('v')
e = matchingName.count('e')

true = t + r + u + e
love = l + o + v + e

finalTrueLove = int(str(true) + str(love))

if finalTrueLove < 10 or finalTrueLove > 90:
    print(f"Your score is {finalTrueLove}, you go like coke and mentos!")
elif finalTrueLove >= 40 and finalTrueLove <=50:
    print(f"Your score is {finalTrueLove}, you are alright together!")
else:
    print(f"Your score is {finalTrueLove}")

