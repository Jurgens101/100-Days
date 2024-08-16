#calculating the highest score of a list 
scoreList = [1,42,-4,24,7,68,243,6,7]
highscore = scoreList[0]

for score in scoreList:
    if score>highscore:
        highscore = score

print(highscore)