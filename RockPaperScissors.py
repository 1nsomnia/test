import random

options = ["rock", "paper", "scissors"]
computer_wins = 0
user_wins = 0
draw = 0

test

while True:
    user_input = input("pick rock/paper/scissors or q to quit: ").lower()
    #print(options[1])
    if user_input == "q":
        break
    if user_input not in options:
        print("kies rock/paper/scissors")
        continue

    computer_pick = options[random.randrange(0,3)]
    #print(computer_pick)
    if user_input == "rock" and computer_pick == "scissors":
        print("you win", user_input, computer_pick)
        user_wins += 1
        continue
    if user_input == "paper" and computer_pick == "rock":
        print("you win", user_input, computer_pick)
        user_wins += 1
        continue
    if user_input == "scissors" and computer_pick == "paper":
        print("you win", user_input, computer_pick)
        user_wins += 1
        continue
    if user_input == computer_pick:
        print("Draw", user_input, computer_pick)
        draw += 1
        continue
    else:
        print("computer wins")
        computer_wins += 1

    



print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print(draw, "draws")
print("Bye")