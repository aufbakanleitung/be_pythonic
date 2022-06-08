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

mass_list = [int(line.rstrip('\n')) for line in open("input_3_RocketEquation.txt")]
from TimeWrapper import timer

def calc_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)

@timer
def total_fuel(mass):
    return sum([calc_fuel(m) for m in mass_list])

print(f"Total fuel necessary is {total_fuel(mass_list)}")