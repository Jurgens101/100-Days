#ask user to enter their weight
userWeight = int(input("Enter your weight in kg: "))

#ask user to enter their height
userHeight = float(input("Enter your height in cm: "))

#calculate the user BMI
BMI = userWeight / (userHeight * userHeight) 
BMI = int(BMI)
print ("Your BMI is :",BMI)