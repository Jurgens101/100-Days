import random
#ask the user to enter 5 names
names = str(input("Enter 5 names then press enter to see who will pay!\n"))
names = names.split()

#randomizing a "winner" to pay the bill
randomizedName = random.randint(0,4)

print(f"{names[randomizedName]} is the lucky one that has to pay the bill!")