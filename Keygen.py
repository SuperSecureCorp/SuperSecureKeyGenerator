#! python 3

# KeyGen.py -> Our extremely complex CD License Key Generator!
## What do you mean people don't use CD's anymore?

import random, sys

class KeyGen():
	def __init__(self):
		global i
		i = int(input("How many serial codes are you looking for? \n"))
		print("")
		self.main(i)
# This allows the user to input how many iterations of a key generation they'd like.
# The more, iterations, the keys! Profits!

	def main(self, count):
		""" Our main iteration function, using simple 
		capital letters, along with the numbers 0-9 """
		seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		for i in range(count):
			print('-'.join(''.join(random.choice(seq) for _ in range(5)) for _ in range(5)))
# Our loop used to iterate through the range of our count parameter, and print our keys to the console
## in sequences of 5 letters/numbers.

		print("\nCreated {} serial keys for you, m'lord.".format(count))
if __name__ == '__main__':
	app = KeyGen()
