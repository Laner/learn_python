'''Problem 11
22 February 2002

In the 2020 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
The product of these numbers is 26  63  78  14 = 1788696.

What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 2020 grid?
'''
lst01 = [int(x) for x in "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08".split(" ")]
lst02 = [int(x) for x in "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00".split(" ")]
lst03 = [int(x) for x in "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65".split(" ")]
lst04 = [int(x) for x in "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91".split(" ")]
lst05 = [int(x) for x in "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80".split(" ")]
lst06 = [int(x) for x in "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50".split(" ")]
lst07 = [int(x) for x in "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70".split(" ")]
lst08 = [int(x) for x in "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21".split(" ")]
lst09 = [int(x) for x in "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72".split(" ")]
lst10 = [int(x) for x in "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95".split(" ")]
lst11 = [int(x) for x in "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92".split(" ")]
lst12 = [int(x) for x in "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57".split(" ")]
lst13 = [int(x) for x in "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58".split(" ")]
lst14 = [int(x) for x in "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40".split(" ")]
lst15 = [int(x) for x in "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66".split(" ")]
lst16 = [int(x) for x in "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69".split(" ")]
lst17 = [int(x) for x in "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36".split(" ")]
lst18 = [int(x) for x in "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16".split(" ")]
lst19 = [int(x) for x in "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54".split(" ")]
lst20 = [int(x) for x in "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48".split(" ")]
all = [lst01, lst02, lst03, lst04, lst05, lst06, lst07, lst08, lst09, lst10, lst11, lst12, lst13, lst14, lst15, lst16, lst17, lst18, lst19, lst20]


def right(*args):
    largest_nr = 0
    for current_str in args:
        # current_str = [int(x) for x in current_str]
        length = len(current_str)
        #print current_str
        for x in xrange(length - 5):
            l = current_str[x:x + 5]
            l = reduce(lambda z, y: z * y, l)
            if l > largest_nr:
                largest_nr = l
    return largest_nr


def down(*args):
    largest_nr = 0
    for start in xrange(len(args) - 3):
      #print "test", start
        tmp_args = args[start:start + 4]
        for x in zip(*tmp_args):
            tmp_val = reduce(lambda z, y: z * y, x)
            if tmp_val > largest_nr:
                largest_nr = tmp_val
    return largest_nr


def diagonally(*args):
    largest_nr = 0
    for start in xrange(len(args) - 3):
        #take four lines at the time
        tmp_args = args[start:start + 4]
        for x in xrange(len(tmp_args)):
            #print start
            #print "----------"
            print tmp_args[0][x] , tmp_args[1][x + 1] , tmp_args[2][x + 2], tmp_args[3][x + 3]
            total = tmp_args[0][x] * tmp_args[1][x + 1] * tmp_args[2][x + 2] * tmp_args[3][x + 3]
            if total > largest_nr:
                largest_nr = total
    return largest_nr


def main(*args):
    right_result = right(*args)
    down_result = down(*args)
    dia_reult = diagonally(*args)
    return max(right_result, down_result, dia_reult)
print main(*all)
