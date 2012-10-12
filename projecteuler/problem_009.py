'''
Problem 9
25 January 2002

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
200, 375, 425
'''
pyttri = [[a, b, c] for a in xrange(1,1001) for b in xrange(1,1001) for c in xrange(1,1001) if a+b+c==1000 and a**2 + b**2 == c**2]
print pyttri
