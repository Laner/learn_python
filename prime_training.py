def isPrime(startnumber):
    startnumber*=1.0
    if startnumber%2==0 and startnumber!=2:
        return False
    for divisor in range(3,int(startnumber**0.5)+1,2):
        if startnumber%divisor==0:
            return False
    return True
#print isprime2(1)

def nextPrime(possible_prime):
    #possible_prime *= 1.0
    is_prime = False
    while not is_prime:
        if possible_prime % 2 == 0 and possible_prime != 2 or possible_prime == 1:
            possible_prime += 1
        else:
            for divisor in xrange(3, int(possible_prime ** 0.5) + 1, 2):
                if not possible_prime % divisor:
                    print "dividable by: ", divisor
                    possible_prime += 1
                    break
            else:
                print "It is a prime -> ", possible_prime
                is_prime = True

x = sum([i for i in xrange(2,200) if isPrime(i)] )
print x