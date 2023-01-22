"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


def find_number(number):
	for i in range(1,21):
		if a%i != 0:
			return False

	return True

a = 20
while True:
	if find_number(a):
		break

	a+=20

print(a)