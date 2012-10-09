def nextPrime(lastPrime=20):
    start_number, isPrime = lastPrime + 1, False
    while not isPrime:
        for divisor in xrange(2, int(start_number ** 0.5) + 1, 2):
            if start_number % divisor == 0 and start_number != 2:
                start_number += 1
                break
            else:  # start_number == divisor + 1:
                isPrime = True
            #if isPrime:
                #print("%i is a prime") % start_number
    yield start_number
    start_number += 1

p = nextPrime()
for x in xrange(1,10):
    print p.next()
