# BruteForceMetcalf
Project Assignment 



Overview

This script is a simple implementation of a time-based brute force attack to guess the password of a binary file vault.o. The password is assumed to consist of only lowercase letters, and the length of the password is fixed at 8 characters.




Requirements

Python 3.x

vault.o binary file





Usage

Make sure the vault.o binary file is in the same location as the brute_force.py script. 

Give execute permissions to the vault.o binary file by executing the following command in a terminal:
chmod +x vault.o

To run the script, execute the following command in a terminal:
python3 brute_force.py

The script will start generating and verifying the password combinations until it finds the correct password. The time taken to guess the password depends on several factors, such as the processing power of the machine and the time taken by the vault.o binary to verify each password.




Note

This script is for educational purposes only and should not be used for any malicious activities. The use of this script may be illegal and can result in severe consequences.

