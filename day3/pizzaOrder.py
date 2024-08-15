#ask the user what size of pizza they want
pizzaSize = str(input("Our Menu includes (S)mall, (M)eddium and (L)arge pizzas.\n Please enter the first letter in capital! \n What size of pizza do you want? :"))

if pizzaSize == "S":
    finalPrice = 15
elif pizzaSize == "M":
    finalPrice = 20
else:
    finalPrice = 25

#ask the user if they want extra cheese
extraCheese = str(input("Do you want extra cheese? (Y)es or (N)o \n"))
if extraCheese == "Y":
    finalPrice +=1 

#ask the user if they want pepperoni
pepperoni = str(input("Do you want pepperoni?  (Y)es or (N)o \n"))
if pepperoni == "Y":
    if pizzaSize == "S":
        finalPrice +=2
    else:
        finalPrice +=3

print(f"Your final prize is: ${finalPrice}")