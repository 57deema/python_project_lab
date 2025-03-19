# DSAI 3202 - Assignment 1 (Part 1)
# Author: Dima
# Task: Multiprocessing and Semaphores (Individual Work)

import time
import random
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

#######################################
# TASK 1 - Multiprocessing (Square Calculation)
#######################################

# 1. Define square function
def square(n):
    return n * n

# 2. Create list of numbers
NUMBERS_SMALL = list(range(1000))  # Reduced size for testing
NUMBERS_LARGE = list(range(10**7))

# Helper to measure time
def measure_time(func, numbers, label):
    start = time.time()
    func(numbers)
    end = time.time()
    print(f"{label} Time: {end - start:.2f} seconds")

# 3a. Sequential for loop
def sequential_square(numbers):
    return [square(n) for n in numbers]

# 3b. Multiprocessing loop with individual processes (inefficient but required)
def multiprocessing_individual(numbers):
    processes = []
    for n in numbers:
        p = multiprocessing.Process(target=square, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

# 3c. Pool with map()
def pool_map_square(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(square, numbers)

# 3d. Pool with apply_async()
def pool_apply_async_square(numbers):
    with multiprocessing.Pool() as pool:
        results = [pool.apply_async(square, args=(n,)) for n in numbers]
        results = [r.get() for r in results]

# 3e. ProcessPoolExecutor
def executor_square(numbers):
    with ProcessPoolExecutor() as executor:
        list(executor.map(square, numbers))

# Run all methods on SMALL and LARGE lists
if __name__ == "__main__":
    print("---- Testing on 10^3 numbers (reduced SMALL set) ----")
    measure_time(sequential_square, NUMBERS_SMALL, "Sequential")
    measure_time(multiprocessing_individual, NUMBERS_SMALL, "Multiprocessing - Individual Processes")
    measure_time(pool_map_square, NUMBERS_SMALL, "Pool Map")
    measure_time(pool_apply_async_square, NUMBERS_SMALL, "Pool Apply Async")
    measure_time(executor_square, NUMBERS_SMALL, "ProcessPoolExecutor")

    print("\n---- Testing on 10^7 numbers ----")
    measure_time(sequential_square, NUMBERS_LARGE, "Sequential")
    measure_time(pool_map_square, NUMBERS_LARGE, "Pool Map")
    measure_time(pool_apply_async_square, NUMBERS_LARGE[:10000], "Pool Apply Async (safe test)")
    measure_time(executor_square, NUMBERS_LARGE, "ProcessPoolExecutor")

#######################################
# TASK 2 - Semaphore and Connection Pool
#######################################

class ConnectionPool:
    def __init__(self, max_connections):
        self.semaphore = multiprocessing.Semaphore(max_connections)

    def get_connection(self):
        self.semaphore.acquire()

    def release_connection(self):
        self.semaphore.release()

def access_database(pool, process_id):
    print(f"Process {process_id} waiting for connection...")
    pool.get_connection()
    print(f"Process {process_id} acquired connection.")
    time.sleep(random.uniform(1, 3))  # Simulate DB operation
    print(f"Process {process_id} releasing connection.")
    pool.release_connection()

def simulate_database_access():
    pool = ConnectionPool(max_connections=3)
    processes = []
    for i in range(6):  # More processes than connections
        p = multiprocessing.Process(target=access_database, args=(pool, i))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print("All database operations completed.")

# Run DB simulation
print("\n---- Testing Semaphore-based Connection Pool ----")
simulate_database_access()