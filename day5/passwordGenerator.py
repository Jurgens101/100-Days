import random

#creating a password generator 
#asking user how many letters long should the password be
passLength = int(input("How many letters would you like in your password? "))
passSymbols = int(input("How many symbols would you like? "))
passNumbers = int(input("How many numbers would you like? "))
password = []
symbols = ['~','@','#','$','%','^','&','(',')','-','_','+','=','|','[',']','\\','<','>',',','.','/','?']
numbers = ['1','2','3','4','5','6','7','8','9','0'] 
letters = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']

for i in range (1,passLength+1):
    password.append(random.choice(letters))
for j in range (1,passSymbols+1):
    password.append(random.choice(symbols))
for k in range (1,passNumbers+1):
    password.append(random.choice(numbers))


random.shuffle(password)
password= ''.join(password)


print(password)