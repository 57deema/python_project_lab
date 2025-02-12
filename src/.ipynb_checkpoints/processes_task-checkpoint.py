import time
from concurrent.futures import ProcessPoolExecutor
from src.functions import calculate_partial_sum

def run_processes(n, num_processes=4):
    """Run parallel sum calculation using multiprocessing."""
    chunk_size = n // num_processes
    start_time = time.perf_counter()

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(calculate_partial_sum, 
                                    [i * chunk_size + 1 for i in range(num_processes)], 
                                    [(i + 1) * chunk_size if i != num_processes - 1 else n for i in range(num_processes)]))

    total_sum = sum(results)
    end_time = time.perf_counter()

    print(f"Multiprocessing Sum: {total_sum}")
    print(f"Execution Time (Multiprocessing): {end_time - start_time:.6f} seconds")