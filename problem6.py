"""The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + 3^2 + 4^2 + .... = 385

The square of the sum of the first ten natural numbers is, (1+2+3+4+5+6+7+8+9+10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


print(sum([x for x in range(1, 101)])**2 - (sum([i*i for i in range(1,101)])))

#more beginner friendly way:

# sum_list = []
# square_list = []

# for i in range(1, 101):
#     sum_list.append(i*i)
#     square_list.append(i)


# sum_of_squares = sum(sum_list)
# square_of_sum = sum(square_list)**2

# print(square_of_sum - sum_of_squares)