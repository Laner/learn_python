"""
Problem 6
14 December 2001

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def square_or_sums(end_nr):
    sum_of_squares = sum([x ** 2 for x in xrange(1, end_nr + 1)])
    square_of_sums = sum([x for x in xrange(1, end_nr + 1)]) ** 2
    return square_of_sums - sum_of_squares
print("Problem 6: %i") % square_or_sums(100)
