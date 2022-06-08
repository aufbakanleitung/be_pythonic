# Create an interactive rock paper scissors game
from random import random

mat = {"rock":0, "paper":1, "scissors":2}
mat_reverse = {0:"rock", 1:"paper", 2:"scissors"}

print('rock, paper or scissors?')
you = input().lower()
computer = int(3*random())
print(mat_reverse[computer])

if mat[you] == computer:
    print("Draw!")
elif mat[you] == 0 and computer == 2 or mat[you] > computer:
    print("You win!")
else:
    print("You lose, haha!")