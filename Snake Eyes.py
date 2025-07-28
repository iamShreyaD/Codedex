import random

# snake eyes means rolling two 1s
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

while total != 2:
    print("Nope")

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

print("You hit the Snake eyes.")