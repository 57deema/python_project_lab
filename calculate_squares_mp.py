# Lab 6 - Multiprocessing Version (Fallback)
# Group: Dima, Areej, Amelda

import time
import multiprocessing as mp

def calculate_squares(start, end):
    return [i ** 2 for i in range(start, end + 1)]

def worker(task_range, queue):
    start, end = task_range
    squares = calculate_squares(start, end)
    queue.put(squares)

if __name__ == '__main__':
    n = int(1e6)  # Reduced for test; you can increase to simulate full lab
    num_processes = 3
    chunk_size = n // num_processes
    processes = []
    queue = mp.Queue()

    start_time = time.time()

    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_processes - 1 else n
        p = mp.Process(target=worker, args=((start, end), queue))
        processes.append(p)
        p.start()

    results = []
    for _ in range(num_processes):
        results.extend(queue.get())

    for p in processes:
        p.join()

    print(f"✅ Final array size: {len(results)}")
    print(f"✅ Last square: {results[-1]}")
    print(f"⏱️ Time taken: {time.time() - start_time:.2f} seconds")