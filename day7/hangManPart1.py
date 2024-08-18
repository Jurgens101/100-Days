#guessing a random word from a list
import random

wordList = ['cherries','knit','manage','friendly','dock','throat','slim','dead','mug','back','collar','swim','unhealthy','truck','inform','likeable','fragile','bone','finger','defiant']
userChoice = ""
finalChoice = []
triesCount = 0
magicWord = random.choice(wordList)
wordLength = len(magicWord)
status = False
mistakes = []
playerLives = 5
hangManArt = [
'''
 +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 / \  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
finalArt = hangManArt[::-1]

for i in range (wordLength):
     finalChoice += "_"

print(finalArt[5])

while not status and playerLives > 0:
    
    userChoice = input("Enter a character: \n")
    for i  in range(wordLength):
        letter = magicWord[i] 
        if letter == userChoice:
                if userChoice in finalChoice:
                    print(f"You have already entered {userChoice}")
                else:
                    finalChoice[i] = letter
                    print(f"You have entered: {finalChoice}")
    if userChoice not in magicWord:
        if userChoice in mistakes:
                    print(f"You have already entered {userChoice}")
        else:
            playerLives -= 1
            mistakes.append(userChoice)
            print(f"{userChoice} is not in the word")
            print(f"You have entered these wrong words: {mistakes}")
            print(f"You have {playerLives} Lives left!")
            print(finalArt[playerLives])
    if "_" not in finalChoice:
        print(f"You found the word! It was {magicWord}")
        status = True  
    if playerLives == 0:
        status = True
        print("Oh no you are out of lives!")
        print(f"The word was: {magicWord}")


