import time
import subprocess

# Character set for password generation
charset = 'abcdefghijklmnopqrstuvwxyz'
password_length = 8 # Assumed password length

# Function to calculate the time taken for password verification
def check_password(password):
    start_time = time.time()
    result = subprocess.run(['./vault.o', password], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end_time = time.time()
    time_taken = end_time - start_time
    return (result.stdout.decode().strip(), time_taken)

# Brute-force attack
for i in range(26 ** password_length):
    password = ''
    temp = i
    for j in range(password_length):
        password = charset[temp % 26] + password
        temp //= 26

    result, time_taken = check_password(password)
    if result == 'Success':
        print(f'Password found: {password}
