# src/processes_task.py
import multiprocessing
from src.functions import generate_random_chars, generate_random_sum

# Function to wrap each task in a process
def process_function(func, *args):
    return func(*args)

# Function to run the processes task
def run_processes():
    # Start processes for both tasks
    process1 = multiprocessing.Process(target=process_function, args=(generate_random_chars,))
    process2 = multiprocessing.Process(target=process_function, args=(generate_random_sum,))
    
    # Run the processes
    start_time = time.time()
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    
    end_time = time.time()
    print(f"Time to execute using processes: {end_time - start_time} seconds.")