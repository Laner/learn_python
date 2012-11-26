"""
Problem 5
30 November 2001
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
answer: 232792560
answer: 232792560
"""
def evenlyDiviseble(end_range):
    dividers = [x for x in range(2, end_range + 1)]
    # print dividers
    # print dividers[-1]
    isFound = False
    count = 1
    while not isFound:
        # if not count % 1000000:
        #     print count
        for x in dividers:
            if count % x:
                count = count + 1
                break
            if x == dividers[-1]:
                print count
                isFound = True
print evenlyDiviseble(20)
