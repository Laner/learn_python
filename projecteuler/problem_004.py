"""
Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def largestPali():
    palilist = []
    for x in reversed(xrange(900, 999)):
        for y in reversed(range(900, 999)):
            nr = y * x
            if nr == int(str(nr)[::-1]):
                palilist.append(nr)
                break
    result = max(palilist)
    print "Problem 4: %i" % result

largestPali()
