"""Problem 3
02 November 2001

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def nextPrime(lastPrime):
    nr, isPrime = lastPrime + 1, False
    while not isPrime:
        for x in xrange(2, nr):
            if not nr % x:
                nr += 1
                break
            if nr == x + 1:
                isPrime = True
            #if isPrime:
                #print("%i is a prime") % nr
    return nr


def findPrimeFactors(total, prime=2):
    if total == 1:
        #print("Bingo: %i" % prime)
        return prime
    if not total % prime:
        #print(prime)
        return findPrimeFactors(total / prime, prime)
    else:
        return findPrimeFactors(total, nextPrime(prime))

prob3 = findPrimeFactors(600851475143)
print("Problem 3: %i") % prob3
