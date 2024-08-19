# creating a calculator 
from calcLogo import logo

def add(a,b):
    return a+b

def subs(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

operations = {
    "+" : add,
    "-" : subs,
    "*" : mult,
    "/" : div
}


def calculator():
    keepGoing = True
    userNumber1 = float(input("What's the first number?: "))
    print(" ")
    for symbol in operations:
        print(symbol)

    while keepGoing:
        operationSymbol = input("Pick an operation \n")
        userNumber2 = float(input("What's the next number?: "))
        calculationFunction = operations[operationSymbol]
        answer = calculationFunction(userNumber1,userNumber2)

        print(f"{userNumber1} {operationSymbol} {userNumber2} = {answer}")

        if input(f"Type 'y' to continue calculating or 'n' to stop\n") == 'y':
            userNumber1 = answer
        else:
            keepGoing = False
            calculator()

calculator()