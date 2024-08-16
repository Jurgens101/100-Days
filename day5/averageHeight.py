#calculating the average height of random people
peopleHeight = [120, 190, 142, 163, 194, 188, 154]
totalHeight = 0

for height in peopleHeight:
    totalHeight += height

averageHeight = totalHeight//len(peopleHeight)
print(averageHeight)