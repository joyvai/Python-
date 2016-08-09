# Bagels is a deduction game.
# you are asking for 3-digit number with no repeating digits
# and try to guess what the number is.
# your opponent or computer gives you three clues:
# Bagels = it means your three digits doesn't match the secret number
# Pico = it means in your three digits one digit match the secret number but this digit in the wrong place.
# Fermi = You won! That means your all three digit match the secret number.
# If the secret number is 456 and your guess is 546 the
# clues would be “fermi pico pico”. The 6 provides “fermi” and the 5 and 4 provide “pico pico”.
# code starts here

import random

def getSecretNum(numDigits):
    # Returns a string that is numDigits long,made up of unique random digits.
    numbers = list(range(10)) # numbers = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers) # after shuffle() it always give you a list.
    # Getting the secret number from the shuffled digits.
    secretNum = ' ' #empty string
    for i in range(numDigits):
        secretNum = secretNum +  str(numbers[i])
    return secretNum
# Calculating the clues to give

def getClues (guess, secretNum):
    
    # Returns a string with the pico, fermi, bagels clues to the user.
    if guess == secretNum:
        return 'You got it'
    clue = [] # clue is a empty list

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0: # if the guess is wrong then it shows Bagels.
        return 'Bagels'

    clue.sort()
    return '  '.join(clue) # it will return a list like ['pico','Fermi','pico']

# The isOnlyDigits() helps determine if the player entered a valid guess.
# here only digits works but these digits are made up string not numeric number.


def isOnlyDigits(num):
    # Returns True if num is a string made up only of digits. Otherwise returns False.
    if num == ' ':
         return False
# for loop iterates over each character in the string num.
# The value of i will have a single character on each iteration.
# line 55 => ['0','1','2','3','4','5','6','7','8','9']
# if i not in line 55 list then it returns False
# if in the list,it returns True.
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True
# if the player wants to play Again

def playAgain():
# This function returns True if the player wants to play again, 
# otherwise it returns False.
    print ('Do you want to play  again?(yes or no)')
    return input().lower().startswith('y')
# The Start of the Game
# Here the program start again

NUMDIGITS = 3
MAXGUESS = 10

# String Interpolation
# String interpolation is a coding shortcut. 
# Normally, if you want to use the string values inside
# variables in another string, you have to use the + concatenation operator:
# at the end of the code i write simple code about String Interpolation

print ("I am thinking of a %s-digit number. Try to guess what it is. " %(NUMDIGITS))
print ('Here are some clues: ')
print ('When I say:     That means: ')
print ('  Pico                One digit is correct but in the wrong position.')
print ('  Fermi              One digit is correct but in the right position.')
print ('  Bagels             No digit is correct.')

# Creating the secret number
# This is infinite while loop.it will stop when a break statement is executed
# line 90=you get a secret number from getSecretNum() function,passing it NUMDIGITS
# this secret number assigned to secretNum.The value of secretNum is a string
# line 95 tells that guesses start now.
while True:
    secretNum = getSecretNum(NUMDIGITS)
    print ("I have thought up a number.Yo have %s guesses to get." %(MAXGUESS))

    numGuesses = 1
    # New while loop inside the while loop
    while numGuesses <= MAXGUESS:
        # The guess variable is set to the blank string on line 101
        # so the while loop’s condition is False the
        # first time it is checked, ensuring the execution enters the loop.
        guess = ' '
        while len(guess) != NUMDIGITS or not  isOnlyDigits(guess):
            print ('Guess #%s:  ' % (numGuesses) )
            guess = input()

            clue = getClues(guess, secretNum)
            print (clue)
            numGuesses = numGuesses + 1
            # This is will break the or stop the second while loop
            if guess == secretNum:
                break
            if numGuesses > MAXGUESS:
                print ('You ran out of guesses. The answer was %s.' %(secretNum))
    # if playAgain() returns False,break out of the while loop .
    # The program terminates.
    
    if not playAgain():
        break

# name = 'ALice'
# event = 'Party'
# where = 'the pool'
# day='Saturday'
# time = '6:00pm'
# print('Hello, ' + name + '. Will you go to the ' + event + ' at ' + where +
# ' this ' + day + ' at ' + time + '?')

# As you can see, it can be hard to type a line that concatenates several strings.
# You can use sting interpolation,which lets you put placeholders like %s.
# These placeholders are called conversion specifiers.
# %s represent a string.%d represent integer .Like c programming lang.

# name = 'ALice'
# event = 'Party'
# where = 'the pool'
# day='Saturday'
# time = '6:00pm'

# print ('Hello, %s. Will you go to the %s at %s this %s at %s?' %(name,event,where,day,time))













            






































    


