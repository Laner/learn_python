'''Problem 10
08 February 2002

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def isPrime(startnumber):
    startnumber *= 1.0
    if startnumber % 2 == 0 and startnumber != 2:
        return False
    for divisor in range(3, int(startnumber ** 0.5) + 1, 2):
        if startnumber % divisor == 0:
            return False
    return True

x = sum([i for i in xrange(2, 200) if isPrime(i)])
print x
