
import random 
import time

def displayIntro():
	print "You are in a land full of dragons.In front of you,"
	print "you see two caves.In one cave, the dragon is friendly"
	print "and will share his treasure with you.The other dragon"
	print ()
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print 'Which cave will you go into?(1 or 2)'
		cave = raw_input()
	return cave

def checkCave(chooseCave): 
	print 'You approach the cave...'
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

