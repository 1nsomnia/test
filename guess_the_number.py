import random
upper = int(input("Give the upper number "))
#upper = int(upper)

number = random.randrange(0, upper)
guesses = 0

while True:
    answer = input("Guess the number 0-" + str(upper) +"? ")
    answer = int(answer)
    guesses = guesses +1
#print(type(answer))

    if answer == number:
        print("correct")
        break
    else:
        if answer < number:
            print("to low")
        else:
            print("to high")

print("You have guessed it in :", guesses ,"turns")