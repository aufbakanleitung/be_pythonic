# Assignment 1
# create a function that prints all numbers that contain only unique numbers
numberlist = [2347821, 4567891, 2938479382, 12328827, 837651, 1234567890, 9234793,
              1823762187, 12372386, 1928379812, 361123, 23456789, 567890, 345678, 4578932]


def all_digits_unique(num):
    num = str(num)
    return len(num) == len(set(num))


def solve(nlist):
    counter = 0
    for n in nlist:
        if all_digits_unique(n):
            counter += 1
    return counter


solve(numberlist)