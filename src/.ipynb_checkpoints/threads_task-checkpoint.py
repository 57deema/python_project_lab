import time
from concurrent.futures import ThreadPoolExecutor
from src.functions import calculate_partial_sum

def run_threads(n, num_threads=4):
    """Run parallel sum calculation using threads."""
    chunk_size = n // num_threads
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(calculate_partial_sum, 
                                    [i * chunk_size + 1 for i in range(num_threads)], 
                                    [(i + 1) * chunk_size if i != num_threads - 1 else n for i in range(num_threads)]))

    total_sum = sum(results)
    end_time = time.perf_counter()

    print(f"Threaded Sum: {total_sum}")
    print(f"Execution Time (Threads): {end_time - start_time:.6f} seconds")