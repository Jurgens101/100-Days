import random

#ask user  to enter an option between paper,scissors or rock
userChoice = input("Enter Paper, Scissors or Rock: ")
botNum = random.randint(0,2)
botChoice = ""

if userChoice == "Rock":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
if userChoice == "Paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

if userChoice == "Scissors":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if botNum == 0:
    botChoice = "Paper"
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif botNum == 1:
    botChoice = "Rock"
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
else:
    botChoice = "Scissors"
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if userChoice == botChoice:
    print(f"You picked {userChoice} and the Robot picked {botChoice} ")
    print("Is a draw")
elif userChoice == "Paper" and botChoice == "Rock":
    print(f"You picked {userChoice} and the Robot picked {botChoice} ")
    print("You Win!")
elif userChoice == "Scissors" and botChoice == "Paper":
    print(f"You picked {userChoice} and the Robot picked {botChoice} ")
    print("You Win!")
elif userChoice == "Rock" and botChoice == "Scissors":
    print(f"You picked {userChoice} and the Robot picked {botChoice} ")
    print("You Win!")
else: 
    print(f"You picked {userChoice} and the robot picked {botChoice} ")
    print("Robot Wins!")




