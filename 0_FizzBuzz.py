# Create a FizzBuzz
# Print the number from 1 to 100 but if it's a multiple of 3 print Fizz, of 5 print Buzz, if it's both print FizzBuzz
# Extra credit; create one that also handles 7 (Balls) and 11 (Booze)

for i in range(1,100):
    out = ""
    if i % 3 == 0: out += "fizz"
    if i % 5 == 0: out += "buzz"
    if i % 7 == 0: out += "balls"
    if i % 11 == 0: out += "booze"
    if out == "": out = i
    print(out)
# Create a FizzBuzz
# Print the number from 1 to 100 but if it's a multiple of 3 print Fizz, of 5 print Buzz, if it's both print FizzBuzz
# Extra credit; create one that also handles 7 (Balls) and 11 (Booze)