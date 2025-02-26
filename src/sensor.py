import random
import time
import threading

latest_temperatures = {}  # Global dictionary for storing latest readings
num_sensors = 3  # Number of sensors

def simulate_sensor(sensor_id, lock):
    """Simulates a temperature sensor that updates its reading every second."""
    global latest_temperatures
    while True:
        temperature = random.randint(15, 40)  # Generate random temperature
        with lock:  # Ensure thread-safe update
            latest_temperatures[sensor_id] = temperature
        time.sleep(1)  # Update every 1 second