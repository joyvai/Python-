import random

print 'I am thinking of a number between 1 and 20'

while True:
	print 'Take a guess.'

	Input = int(raw_input ())

	if (Input >= 1 and Input <=15):
		print 'Your guess is too low'	

	elif (Input == 16):
		print 'Good job!You guessed my number in 4 guesses!'
		break
	
	elif (Input>16 and Input <=20):
		print 'Your guess is too high'
			
	elif (Input ==0):
		print 'Only 1 to 20'
	else:
		print 'Give input 1 to 20'


