# Import necessary libraries
import random
import string

# Get user input for the string and key
str_input = input("Enter a string: ")
key = int(input("Enter a key (the number of characters you want to encrypt or decrypt by): "))

# Split the input string into a list of words
str_list = str_input.split(" ")

# Prompt the user for encryption or decryption choice
print("Do you want to encrypt or decrypt the string?")
print("Input 1 for encrypt and 2 for decrypt")
choice = int(input("Enter your choice: "))

# Define special characters that can be included in the encryption
special_characters = "@#$%&*!?/;:"

# Encryption
if choice == 1:
    new_words = []
    for word in str_list:
        if len(word) >= 3:
            # Generate random prefixes and suffixes for encryption
            prefix = ''.join(random.choices(string.ascii_lowercase + string.digits + special_characters, k=key))
            suffix = ''.join(random.choices(string.ascii_lowercase + string.digits + special_characters, k=key))
            
            # Perform encryption on the word
            encrypted_word = prefix + word[1:] + word[0] + suffix
            new_words.append(encrypted_word)
        else:
            # If the word is less than 3 characters, reverse it
            new_words.append(word[::-1])
    
    # Print the encrypted string
    print(" ".join(new_words))

# Decryption
elif choice == 2:
    new_words = []
    for word in str_list:
        if len(word) >= key:
            # Perform decryption on the word
            decrypted_word = word[key:-key]
            decrypted_word = decrypted_word[-1] + decrypted_word[:-1]
            new_words.append(decrypted_word)
        else:
            # If the word is less than the key, reverse it
            new_words.append(word[::-1])
    
    # Print the decrypted string
    print(" ".join(new_words))
