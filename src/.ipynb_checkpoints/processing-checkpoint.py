import time
import threading
from queue import Queue

temperature_averages = {}  # Stores average temperatures
num_sensors = 3

def process_temperatures(queue, lock, condition):
    """Continuously calculates average temperature from the queue."""
    global temperature_averages
    while True:
        with condition:
            condition.wait()  # Wait for new data

        with lock:
            if not queue.empty():
                temp_list = list(queue.queue)  # Get all values in queue
                average_temp = sum(temp_list) / len(temp_list)
                temperature_averages['average'] = average_temp
        time.sleep(5)  # Update every 5 seconds