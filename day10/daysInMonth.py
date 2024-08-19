#ask user for a year

def isLeapYear(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False
    
def daysInMonth(isLeapYear,month):
    if isLeapYear == True:
        monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        return monthDays[month-1]
    else:
        monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        return monthDays[month-1]
    
userYear = int(input("Enter a year to check if its leap or not:\n"))
userMonth = int(input("Enter a month:\n"))

days = daysInMonth(userYear,userMonth)
print(days)