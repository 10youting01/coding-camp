# 猜數字遊戲
from random import randrange

n = randrange(100)
guess = int(input("Please guess a number between 0 and 100\n"))

while guess != n:
    if guess < n:
        print("Bigger!")
        guess = int(input("Guess again!\n"))
    else:
        print("Smaller!")
        guess = int(input("Guess again!\n"))

print("You're right! It's", n)