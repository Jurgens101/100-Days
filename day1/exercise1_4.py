#Asking for  2 variables named a and b 
var1 = int(input("Enter number a: "))
var2 = int(input("Enter number b: "))
print(" a = ", var1)
print(" b = ", var2)

#simple swap of variables with a third one
var3 = var1
var1 = var2
var2 = var3

print("After swap we have a= ", var1," and b= ", + var2)