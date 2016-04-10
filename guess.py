from random import randint  

guessesTaken = 0 

print "Hello! What is your name?"
myname = raw_input()

number = randint (1,20)
print 'Well, '+myname+',I am thinking of a number between 1 and 20.'

while guessesTaken < 6:
	print "Take a guess." 
	guess = raw_input()
	guess = int (guess)
	guessesTaken += 1

	if guess < number:
		print "Your guess is too low."
	if guess > number:
		print "Your guess is too high."
	if guess == number:
		break
if guess == number:
	guessesTaken = str(guessesTaken)
	print 'Good job, ' + myname + '! you guessed my number in ' +guessesTaken+' guesses!'

if guess != number:
	number = str (number)
	print 'Nope. The number i was thinking of was '+ number
