import time
from src.functions import calculate_partial_sum

def run_sequential(n):
    """Run sequential sum calculation."""
    start_time = time.perf_counter()  # More accurate timing
    result = calculate_partial_sum(1, n)
    end_time = time.perf_counter()
    
    print(f"Sequential Sum: {result}")
    print(f"Execution Time (Sequential): {end_time - start_time:.6f} seconds")