"""
Problem 7
28 December 2001

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime numbe
"""

def findNrPrime(nthPrime):
    primeList, candidate = [2], 3
    while len(primeList) < nthPrime:
        for x in xrange(2, candidate):
            if candidate % x == 0:
                break
            if x == candidate - 1:
                primeList.append(candidate)
        candidate += 1
    print primeList[-1]
# findNrPrime(10001)
# matrix = [[x for x in i] for i in range(1, 4)] # <- Your code goes inside those brackets!
# print matrix
