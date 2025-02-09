# src/functions.py
import random
import string

# Function to generate 1000 random characters and join them into a string
def generate_random_chars():
    return ''.join(random.choices(string.ascii_letters, k=1000))

# Function to generate 1000 random numbers and add them
def generate_random_sum():
    return sum(random.choices(range(1, 101), k=1000))