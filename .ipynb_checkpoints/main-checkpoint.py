import threading
from queue import Queue
from src.sensor import simulate_sensor
from src.processing import process_temperatures
from src.display import initialize_display, update_display
from src.sync_utils import lock, condition
from src.sequential_task import run_sequential

if __name__ == "__main__":
    run_sequential()

num_sensors = 3
queue = Queue()

# Start sensor threads
sensor_threads = []
for i in range(num_sensors):
    thread = threading.Thread(target=simulate_sensor, args=(i, lock), daemon=True)
    sensor_threads.append(thread)
    thread.start()

# Start processing thread
processing_thread = threading.Thread(target=process_temperatures, args=(queue, lock, condition), daemon=True)
processing_thread.start()

# Start display update thread
display_thread = threading.Thread(target=update_display, args=(lock, condition), daemon=True)
display_thread.start()

# Keep the main program running
while True:
    pass  # Infinite loop to keep threads alive