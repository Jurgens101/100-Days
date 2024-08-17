#guessing a random word from a list
import random

wordList = ['cherries','knit','manage','friendly','dock','throat','slim','dead','mug','back','collar','swim','unhealthy','truck','inform','likeable','fragile','bone','finger','defiant']
userChoice = ""
finalChoice = []
triesCount = 0
magicWord = random.choice(wordList)
wordLength = len(magicWord)
status = False
playerLives = 5

print(magicWord)
print(len(magicWord))

for i in range (wordLength):
     finalChoice += "_"
print(finalChoice)


while not status and playerLives > 0:
    
    userChoice = input("Enter a letter: \n")
    for i  in range(wordLength):
        letter = magicWord[i] 
        if letter == userChoice:
            finalChoice[i] = letter
        else:
            playerLives -=1   
    if "_" not in finalChoice:
        status = True
    print(finalChoice)
    print(f"You have {playerLives} Lives left!")

    if playerLives == 0:
        status = True
        print("Oh no you are out of lives!")

