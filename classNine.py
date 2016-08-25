

class Name:
	while True:
		a = "joy"
		b = 23
		print "{} is a {} years old.".format(a,b)
		if len(a)>0:
			print 'Do you know about him more?'
			answer = raw_input()
			if answer.lower() == 'yes':
				print 'Tell me about him.'
				brother = 'robin'
				sister = 'liza'
				print '{} has brother {} and sister {}'.format(a,brother,sister)
				print 'I have to go.see you later'
				print 'Thanks for your information'
				break
			else:
				print 'Oh! I see.ok,see you later!'
				break
	def House(self):
		house_name = "Davenport"
		city = 'Boston'
		country = 'England'
		name = 'joy'
		mom = "Mom"
		print "{} calling mom.".format(name)
		print "{}!Where are you?".format(mom)
		print '{}! I have to tell you something!'.format(mom)
		print "What?"
		print "I get a job!"
		print 'God! That\'s great!'
		print "But there is a problem" 
		print "What?"
		print 'I will go {}.\n.There is a city name {}'.format(country,city)
		print 'Come home!'
		print '{}!!Listen to me!!!'.format(mom)

myClass = Name()
myClass.House()
