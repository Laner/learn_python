def plusTwo(max):
    for i in xrange(max):
        yield i +2

for index, i in enumerate(plusTwo(10)):
    print index, i