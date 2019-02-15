import random 
#we will store the number of guesses a player has made in this variable 
#since the player hasn't made any guesses at this point we store integer zero.


guessesTaken = 0

print('hello! what is your name?')

#take the input from the user and store it in myName variable.
myName = input("ENTER YOUR NAME: ")

#store the random number in variable number
number = random.randint(1, 20)

#welcome the player to the game
print('Well,'+ myName +',I am thinking of a number 1 and 20.')

#while condition loop
while guessesTaken < 6:

    print("take a guess.")

    guess = input() 

#calls a new function named int().
#The int function takes one argument and returns an integer value form of that argument.
    guess = int(guess)


#once the player takes a guess, the number of guesses should be increased by one
#incrementing the variable.
    guessesTaken = guessesTaken + 1


    if guess < number:
        print("your guess is too low")

    if guess > number:
        print("your guess is too high")

#the break statement tells the execution to jump immediately 
#...out of the while-block to the first line after the end of thr while-block

    if guess == number:
        break

if guess == number:

# calls the str() function, which returns the string form of guessesTaken
    guessesTaken = str(guessesTaken)

    print('Good job,' + myName + '!you guessed my number in' + guessesTaken+ 'guesses!')

if guess != number:

    number = str(number)

    print("Nope. The number I was thinking of was" + number)



