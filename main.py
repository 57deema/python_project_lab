from src.functions import *
from src.sequential_task import *
from src.threads_task import *
from src.processes_task import *
import time
import random
import string

def performance_analysis():
    num_threads = 4  
    num_processes = 4 
    P = 0.9 

    # Measure execution times
    print("Running Sequential Execution...")
    start = time.time()
    run_sequential()
    T_sequential = time.time() - start

    print("\nRunning Threading Execution...")
    start = time.time()
    run_threads()
    T_threads = time.time() - start

    print("\nRunning Multiprocessing Execution...")
    start = time.time()
    run_processes()
    T_processes = time.time() - start

    # Compute Speedups
    S_threads = T_sequential / T_threads
    S_processes = T_sequential / T_processes

    # Compute Efficiencies
    E_threads = S_threads / num_threads
    E_processes = S_processes / num_processes

    # Compute Amdahl’s Speedup
    S_A_threads = 1 / ((1 - P) + (P / num_threads))
    S_A_processes = 1 / ((1 - P) + (P / num_processes))

    # Compute Gustafson’s Speedup
    S_G_threads = (1 - P) + (P * num_threads)
    S_G_processes = (1 - P) + (P * num_processes)

    # Print results
    print("\n=== Performance Analysis Results ===")
    print(f"Sequential Time: {T_sequential:.4f} sec")
    print(f"Threading Time: {T_threads:.4f} sec, Speedup: {S_threads:.2f}, Efficiency: {E_threads:.2f}")
    print(f"Multiprocessing Time: {T_processes:.4f} sec, Speedup: {S_processes:.2f}, Efficiency: {E_processes:.2f}")
    print(f"Amdahl’s Law Speedup (Threads): {S_A_threads:.2f}")
    print(f"Amdahl’s Law Speedup (Processes): {S_A_processes:.2f}")
    print(f"Gustafson’s Law Speedup (Threads): {S_G_threads:.2f}")
    print(f"Gustafson’s Law Speedup (Processes): {S_G_processes:.2f}")
    

# task 2_a: sequential
print("task 2_a: sequential")
run_sequential()

# task 2_b: threading
print("task 2_b: threading")
run_threads()

# task 2_c: processes
print("task 2_c: processes")
run_processes()

# task 2_d: Performance analysis
print("task 2_d: Performance analysis")
performance_analysis()