#checking if a number is prime or not
def checkPrime(n):
    isPrime = True
    for i in range (2,n):
        if n % i == 0:
            isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

userNumber = int(input("Enter a number to check if its prime or not: \n"))
checkPrime(userNumber)