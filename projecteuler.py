"""Problem 1
05 October 2001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
Prob1 = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
print "Problem 1: %i" % Prob1

"""Problem 2
19 October 2001

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
a, b, fib = 1, 2, []
while a <= 4000000:
  fib.append(a)
  a, b = b, a + b
Prob2 = sum([x for x in fib if x % 2 == 0])
print "Problem 2: %i" % Prob2
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
	if isPrime:
		#print("%i is a prime") % nr
		return nr

def findPrimeFactors(total, prime=2):
	if total == 1:
		print("Bingo: %i" % prime)
		return prime
	if not total % prime:
		print(prime)
		findPrimeFactors(total / prime, prime)
	else:
		findPrimeFactors(total, nextPrime(prime))

print(findPrimeFactors(600851475143))

"""
Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
for x in reversed(range(900,999)):
        for y in reversed(range(900,999)):
                nr = y*x
                if nr == int(str(nr)[::-1]):
                        print nr
                        break
        