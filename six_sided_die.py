from random import randint

while True:
	roll = raw_input("\nwould you like to roll the die?('y'/'n') ")
	if roll == 'y':
		print 'You rolled a ' + str(randint(1,6))
	elif roll == 'n':
		break
	else:
		print 'try again...'
