import random

player = 0
computer = 0

#instructions for player
print("===================")
print("Rock Paper Scissors")
print("===================")

print("1)' ✊")
print("2)' ✋")
print("3)' ✌️")

player = int(input("Pick a number between 1 to 3: "))

if player == 1:
    print("You chose: ✊")  #rock

elif player == 2:
    print("You chose: ✋")  #paper

elif player == 3:
    print("You chose: ✌️")  #scissors

else:
    print("Error. Please rerun the program.")


computer = random.randint(1, 3)

if computer == 1:
    print("Computer chose: ✊")  #rock

elif computer == 2:
    print("Computer chose: ✋")  #paper

elif computer == 3:
    print("Computer chose: ✌️")  #scissors

else:
    print("Error. Please rerun the program.")


if player == 1 and computer == 3:
    print("The player won!")

elif player == 2 and computer == 1:
    print("The player won!")

elif player == 3 and computer == 2:
    print("The player won!")


if player == 1 and computer == 2:
    print("The computer won!")

elif player == 2 and computer == 3:
    print("The computer won!")

elif player == 3 and computer == 1:
    print("The computer won!")


if player == 1 and computer == 1:
    print("It's a tie! Try again!")

elif player == 2 and computer == 2:
    print("It's a tie! Try again!")

elif player == 3 and computer == 3:
    print("It's a tie! Try again!")

