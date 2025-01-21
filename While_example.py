# Virtual dice game, you whin if you roll 6, you lose 1 life if you roll not 6
# you have 3 lives
from random import randint

lives = 3
while lives > 0:
    dice_roll = randint(1,6)
    if dice_roll == 6:

        print("Congrats!, You rolled a 6 you win")
        break
    else:
        lives = lives -1
        print(f" You rolled a {dice_roll}. You lose a life, lives left {lives}.")

else:
    print("You lose!")