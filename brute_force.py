import itertools
import string
import time
import os

# Define the set of characters to use for the password
chars = string.ascii_lowercase

# Define the length of the password
password_length = 8

# Create a generator that yields all possible combinations of the characters
password_combinations = itertools.chain.from_iterable(itertools.product(chars, repeat=i) for i in range(1, password_length + 1))

start_time = time.time()

# Iterate through each combination of characters
for combination in password_combinations:
    password = ''.join(combination)
    result = os.system(f"./vault.o {password}")

    if result == 0:
        print(f"Success! The password is: {password}")
        print(f"Time elapsed: {time.time() - start_time:.2f} seconds")
        break

print(f"Time elapsed: {time.time() - start_time:.2f} seconds")
