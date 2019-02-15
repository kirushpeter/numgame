import random

no_of_guesses = 0

num = random.randint(1, 20)

print("hello! what's your name?")

name = input()

print("hello " + name + " welcome to the game!!")


while no_of_guesses < 6:

    print("type your Guess: ")

    guess = input()

    guess = int(guess)

    no_of_guesses += 1

    if guess < num:

        print(name + " your guess too low")

    if guess > num:

        print(name + " your guess too high")

    if guess == num:
        
        break

if guess == num:

    no_of_guesses = str(no_of_guesses)

    print("congratulations " + name + " for the correct guesses in " + no_of_guesses +" guesses,Bravo!!" )


if guess != num:

    num = str(num)

    print("wrong guess hommy, the number I was looking is " + num)



