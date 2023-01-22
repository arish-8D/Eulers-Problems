"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

num = 600851475143

prime_nums_list = []
factor = 2

while factor <= num:
	if num%factor == 0:
		prime_nums_list.append(factor)
		num = num/factor
	else:
		factor+=1

print(max(prime_nums_list))