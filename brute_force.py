import itertools
import string
import time
import subprocess

# Define the set of characters to use for the password
chars = string.ascii_lowercase

# Define the length of the password
password_length = 8

# Create a generator that yields all possible combinations of the characters
password_combinations = itertools.chain.from_iterable(itertools.product(chars, repeat=i) for i in range(1, password_length + 1))

start_time = time.time()

for password in password_combinations:
    password = "".join(password)
    process = subprocess.Popen(["./vault.o", password], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(f"Success! The password is {password}")
        break
    else:
        print(f"Wrong Password: {password}")

end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")
