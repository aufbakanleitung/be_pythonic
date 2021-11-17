# Use the walrus operator (:=) to improve this code
# The walrus  allows you to both assign and return a variable in the same expression
# Like so: print(beerPrice := 9.99)
print(beerPrice := 9.99)

def count_long_words(chunk):
    count = 0
    for word in chunk.split():
        if len(word) >= 7:
            count += 1
    return count

# Refactor this using :=
def run():
    openedBook = open("input_assignment7.txt")
    longWordCount = 0
    while chunk := openedBook.read(8192):
        longWordCount += count_long_words(chunk=chunk)
    print(longWordCount)

if __name__ == "__main__":
    run()