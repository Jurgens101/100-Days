#ask the user for their age and later calcualte their amount of time "left"
userAge = int(input("Enter your age: "))
fatalYear = 90
userYearsLeft = fatalYear - userAge
userDaysLeft = userYearsLeft * 365
userWeeksLeft = userYearsLeft * 52
userMonthsLeft = userYearsLeft * 12 

print(f"You have {userDaysLeft} days left, {userWeeksLeft} weeks left, and {userMonthsLeft} months left until 90!")