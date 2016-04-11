# This program imports two modules. The random module will provide the random.randint()
# function.. You will also want time-related functions
# that the time module includes, so line 2 imports the time module.

import random 
import time

""" 
Line 14 is a def statement. The def statement defines a new function that you can call later in the
program. When you define this function, you specify the instructions in its def-block. When you
call this function, the code inside the def-block executes.
"""
# Remember, the def statement doesn’t execute the code.
# It only defines what code to execute when you call the function.


def displayIntro():
	print "You are in a land full of dragons.In front of you,"
	print "you see two caves.In one cave, the dragon is friendly"
	print "and will share his treasure with you.The other dragon"
	
"""
Line 26 defines another function called chooseCave() . This function’s code asks the player
which cave they want to go in, either 1 or 2.

This function needs to make sure the player typed 1 or 2, and not something else. A loop here will
keep asking the player until they enter one of these two valid responses. This is called input
validation.

"""

def chooseCave():
	cave = '' # cave is a blank string
	"""This while loop have two condition.This two condition connected by one boolean operator which name is 'and'.
	one condition => cave != 1
     +		and 
	second condition => cave != 2
	"""
	while cave != '1' and cave != '2': # This symbol name is not equal '!='.it's a boolean operator.
	# Boolean operator checks or uses only for True and False.If the logic is True it's return True.if false it's false
	# Boolean operators compare values and evaluate to a single Boolean value.
		print 'Which cave will you go into?(1 or 2)'
		cave = raw_input() # it's taking input from user
	return cave
"""
The next function the program defines is named checkCave() . Notice the text chosenCave
between the parentheses. This is a parameter: a local variable that is assigned the argument
passed when this function is called.
""" 

def checkCave(chooseCave): 
	print 'You approach the cave...'
	
	"""The time module has a function called sleep() that pauses the program. Line 21 passes the
	   integer value 2 so that time.sleep() will pause the program for 2 seconds. 
	 """
	time.sleep(2) # Suspend execution of the current thread for the given number of seconds.
	# after 2 seconds it' suspends.
	print 'It is dark and spooky...'
	time.sleep(2)
	print 'A large dragon jumps out in front of you! He opens his jaws and ....'
	time.sleep(2)

	friendlyCave = random.randint(1,2)

	if chooseCave == str (friendlyCave):
		print 'Gives you his treasure'
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':

	displayIntro() # calling displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)
	print 'Do you want to play again?(yes or no)'
	playAgain = raw_input()
	print 'Thanks for playing the game.'

