import subprocess
import time
import itertools

start = time.time()

alphabet = "abcdefghijklmnopqrstuvwxyz"
password_length = 6

for password_tuple in itertools.product(alphabet, repeat=password_length):
    password = "".join(password_tuple)
    result = subprocess.run(["./vault.o", password], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if b"Success" in result.stdout:
        print("Found password:", password)
        break

end = time.time()
print("Elapsed time:", end - start, "seconds")
