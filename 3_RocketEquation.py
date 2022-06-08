# The rocket equation

# If you launch a something into space you need fuel. The higher the mass the more fuel you need.
# To find the fuel for this assignment take its mass, divide by three, round down, and subtract 2.
# Example: For a mass of 1969, the fuel required is 654
#
# However the fuel also has mass itself, which requires fuel to get it in the air.
# So the total you need is:
# 654 + 216 + 70 + 21 + 5 = 966 fuel
#
# What is the sum of the fuel requirements in the list?
from time import time

mass_list = [int(line.rstrip('\n')) for line in open("input_assignment3.txt")]
