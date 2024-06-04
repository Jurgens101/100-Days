#Greeting message
print("Welcome to the tip calculator!")

#Asking user the amount of the bill
bill=float(input("What is the total bill? "))

#Asking user how many people are sharing the bill
share=float(input("How many people are sharing the bill? "))

#Calculating how much each one has to pay
Amount = bill/share

#Asking user how much to tip
tip=float(input("What percentage do you want to tip? ")) * (Amount / 100)

#Calculating the final amount
finalAmount = Amount + tip
 
#Getting the final amount per person
print("Each person has to pay: ", finalAmount)