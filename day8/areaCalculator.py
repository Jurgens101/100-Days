#calculating the paint area with a function
import math

wallHeight = int(input("Enter the wall's height: \n"))
wallWidth = int(input("Enter the wall's width: \n"))
paintCoverage = 5

def calculateBuckets(a,b,c):
    area = a * b
    cans = math.ceil(area/c)
    print(f"You will need {cans} cans of paint")

calculateBuckets(wallHeight,wallWidth,paintCoverage)