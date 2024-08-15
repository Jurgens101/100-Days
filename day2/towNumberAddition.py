#ask user for a 2 digit number
userNumber = int(input("Enter a two digit number: "))
userNumber = str(userNumber)
numOne = userNumber[0]
numTwo = userNumber[1]
finalNumber = int(userNumber[0]) + int(userNumber[1])
print ("Your Final number is: ",numOne ," + ",numTwo ," = ",finalNumber)