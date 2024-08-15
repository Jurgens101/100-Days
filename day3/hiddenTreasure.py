print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')

print("Welcome to the forgoten island! You see a red gate and a blue gate.")
userGate = str(input("Which one do you chose?\n"))
if userGate == "blue":
    print("You lost, game over!")
elif userGate == "red":
    print("Congrats, you picked the right path.\nNow you see a yellow key and a pink key.")
    userKey = str(input("Which key do you take?\n"))
    if userKey == "yellow":
        print("You lost, game over!")
    elif userKey == "pink":
        print("Gongrats, you picked the right key.\nNow for the final stage you see two dark wholes,\none round and one triangle. \n You have to jump in one of those")
        userWhole = str(input("Which one do you chose\n"))
        if userWhole == "round":
            print("Congrats you won the treasure!")
        else:
            print("Bad luck, you were almost there")