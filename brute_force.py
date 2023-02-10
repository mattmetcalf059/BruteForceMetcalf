import subprocess
import string
import time

def crack_password():
    start = time.time()
    chars = string.ascii_lowercase
    attempts = 0
    password = []
    while True:
        for char in chars:
            attempts += 1
            guess = "".join(password + [char])
            result = subprocess.run(["./vault.o", guess], capture_output=True)
            output = result.stdout.decode().strip()
            if output == "Success":
                print("Password found:", guess)
                return
            elif output == "Wrong password":
                continue
            else:
                print("Unexpected output:", output)
                return
        password.append(chars[0])

if __name__ == "__main__":
    crack_password()
