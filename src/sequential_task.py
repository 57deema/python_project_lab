# src/sequential_task.py
import time  # Make sure to import time module
from src.functions import generate_random_chars, generate_random_sum

# Function to run the sequential task
def run_sequential():
    # Measure time for generating random characters
    start_time = time.time()
    generate_random_chars()
    end_time = time.time()
    print(f"Time to generate random characters (sequential): {end_time - start_time} seconds.")
    
    # Measure time for generating random sum
    start_time = time.time()
    generate_random_sum()
    end_time = time.time()
    print(f"Time to generate random sum (sequential): {end_time - start_time} seconds.")