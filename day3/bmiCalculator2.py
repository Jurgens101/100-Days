#ask user for their weight
userWeight = int(input("Enter your weight in kg: "))

#ask user for their height
userHeight = float(input("Enter your height in cm: "))

#calculate bmi
userBMI = (userWeight // userHeight) // userHeight
print(f"Your BMI is : {userBMI}")
if userBMI < 18.5: 
    print("You are underweight!")
elif userBMI < 25:
    print("You have a normal weight!")
elif userBMI < 30:
    print("You are overweight!")
elif userBMI < 35:
    print("You are obese!")
else:
    print("You are clinically obese!")
