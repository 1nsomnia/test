from ast import Break
import random

number = random.randrange(0, 11)
guesses = 0

while True:
    answer = input("Guess the number 0-10 ")
    answer = int(answer)
    guesses = guesses +1
#print(type(answer))

    if answer == number:
        print("correct")
        break
    else:
        if answer < number:
            print("te laag")
        else:
            print("te hoog")

print("je hebt het in:", guesses ," keer geraden")