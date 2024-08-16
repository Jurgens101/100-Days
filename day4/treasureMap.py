#shaping a 303 map
row0 = [0,0,0]
row1 = [0,0,0]
row2 = [0,0,0]
        
finalMap = [row0,row1,row2]
print(f"{row0}\n{row1}\n{row2}")
userSelection = str(input("Select where to place the X: "))
userSelection = userSelection.split()
first = int(userSelection[0])
second = int(userSelection[1])

finalMap[second-1][first -1] = "X"

print(f"{row0}\n{row1}\n{row2}")
