# Creating a generator
from time import sleep


# 1. Change this function from eager (or greedy) compute to lazy evaluation - without inserting a print
# Q: How large is this program?
def compute():  # Eager compute
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv


# 2. Make sure these functions can only be run in order
class Api:
    def run_this_first(self):
        print("first")

    def run_this_second(self):
        print("second")

    def run_this_last(self):
        print("last")


def compute2():  # Generator (or lazy) compute
    for i in range(10):
        sleep(.5)
        yield i


for val in compute2():
    print(val)
