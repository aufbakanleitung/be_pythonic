# Assignment 2 - Ciphertext
# Create a function that encrypts text by moving each letter 3 position higher in the alphabet

example_text = "In cryptography, encryption is the process of encoding a message or information in such a way that " \
               "only authorized parties can access it and those who are not authorized cannot."


def encrypt(text):
    encrypted_text = ""
    for letter in text:
        if letter == " ":
            encrypted_text += " "
        else:
            encrypted_text += chr((ord(letter) + 2))
    return encrypted_text


print(encrypt(example_text))