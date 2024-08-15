#importing random library
import random

#flipping a coin between 0/Heads or 1/Tails
flipACoin = random.randint(0,1)

if flipACoin == 0:
    print(f"You flipped Heads! ({flipACoin})")
else:
    print(f"You flipped Tails ({flipACoin})")