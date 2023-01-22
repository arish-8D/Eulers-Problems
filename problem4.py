"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def is_palindrome(number):
	str_palind = str(number)
	if str_palind == str_palind[::-1]:
		return True

products = []

for i, j in zip(range(1,1000,), range(1000, 1, -1)):
		if is_palindrome(i*j):
			products.append(i*j)
		else:
			pass


print(max(products))
