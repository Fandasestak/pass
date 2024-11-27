import random

target = random.randint(1, 10)

while True:
    guess = int(input("Hádej číslo (1-10, nebo 0 pro ukončení): "))
    if guess == 0:
        break
    if guess < 1 or guess > 10:
        continue
    if guess < target:
        print("Hádáš příliš nízko!")
    elif guess > target:
        print("Hádáš příliš vysoko!")
    else:
        print("Správně!")
        break