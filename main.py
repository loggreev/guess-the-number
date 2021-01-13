# https://rosettacode.org/wiki/Guess_the_number/With_feedback

# Write a game (computer program) that follows the following rules:
# # The computer chooses a number between given set limits.
# # The player is asked for repeated guesses until the the target number is guessed correctly
# # At each guess, the computer responds with whether the guess is:
# # # higher than the target,
# # # equal to the target,
# # # less than the target,   or
# # # the input was inappropriate.

import re
import random

def main():
	print('***Guess the number program***')
	print('In this program, you enter a range of numbers to make a guess from, inclusively.')
	print('If your guess is incorrect, you will be informed where the answer is relative to your guess.')
	print('Once you guess correctly, you will see the number of guesses it took.')
	print()

	gameloop = True

	while gameloop:
		range = get_two_numbers()
		range.sort()
		min = range[0]
		max = range[1]
		answer = random.randint(min, max)

		guessloop = True
		num_guesses = 0
		while guessloop:
			guess = get_valid_int(f'Make a guess from {min} to {max}: ')
			if guess < min or guess > max:
				print('Guess out of range.')
				continue
			
			num_guesses += 1
			if guess < answer:
				print(guess, 'is less than the answer.')
			elif guess > answer:
				print(guess, 'is greater than the answer.')
			else:
				print(guess, 'is the answer! It took you', num_guesses, 'guesses.')
				print()
				guessloop = False
		
		# ask user if they want to play again
		invalid_inputs = True
		while invalid_inputs:
			keep_playing_input = input('Keep playing? (y/n) ');
			if re.search('^y(es)?$', keep_playing_input, re.IGNORECASE):
				print('Starting new game...')
				print()
				invalid_inputs = False
				continue
			elif re.search('n(o)?$', keep_playing_input, re.IGNORECASE):
				print('Thanks for playing!')
				print()
				gameloop = False
				invalid_inputs = False
				continue
			else:
				print('Invalid input.')
				continue
				
# get the number range for the guessing game
def get_two_numbers():
	num1 = get_valid_int('Enter the first integer: ')
	num2 = get_valid_int('Enter the second integer: ' )
	print()
	return [num1,num2]

# ask the user for a integer until it is valid
def get_valid_int(message = 'Enter an integer: '):
	while True:
		try:
			n = int(input(message))
		except ValueError:
			print('The number must be an integer!')
			continue
	
		return n

main()