import random

secretNumber = random.randint(1,20)

print 'I am thinking of a number between 1 and 20.'

for guessesTaken in range (1,7):
	print 'Take a guess.'
	guess = int(raw_input())
	if guess < secretNumber:
		print 'your guess is too high.'
	elif guess > secretNumber:
		print 'Your guess is too high.'
	else:
		break

if guess == secretNumber:
	print 'Good job!You guessed my number in '+str(guessTaken) + 'guesses!'
else:
	print 'Nope.The number I was thinking of was ' +str(secretNumber)
	
	
	
	
	
	
	
	
	
	
