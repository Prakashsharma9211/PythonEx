'''
num = int(input("Enter the Number :"))
if (num>0):
	print("Num is Positive")
elif(num<0): 
	print("Num is Negative")
else:
	print("Value is Zero")
'''


'''
import random
print(random.randint(1,15))
'''
import random
guessesTaken = 0
myName = input('Hello! What is your name?')
number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
while guessesTaken < 6:
		print('Take a guess.')
		guess = input()
		guess = int(guess)
		guessesTaken = guessesTaken + 1
		if guess < number:
			print('Your guess is too low.')
		if guess > number:
			print('Your guess is too high.')
		if guess == number:
			break
if guess == number:
		guessesTaken = str(guessesTaken)
		print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
		number = str(number)
		print('Nope. The number I was thinking of was ' + number)