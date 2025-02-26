import time
import os
from src.sync_utils import lock
from src.sensor import latest_temperatures
from src.processing import temperature_averages

def initialize_display():
    """Initial display layout."""
    print("\nCurrent Temperatures:\n")
    for i in range(3):
        print(f"Sensor {i}: --°C")
    print("\nAverages:\n")
    for i in range(3):
        print(f"Sensor {i} Average: --°C")

def update_display(lock, condition):
    """Update display every 5 seconds without clearing the console."""
    while True:
        os.system('clear')  # Use 'cls' on Windows

        with lock:
            print("\nCurrent Temperatures:\n")
            for i in range(3):
                temp = latest_temperatures.get(i, "--")
                print(f"Sensor {i}: {temp}°C")

            print("\nAverages:\n")
            for i in range(3):
                avg_temp = temperature_averages.get('average', "--")
                
                # ✅ FIX: Ensure avg_temp is a float before formatting
                if isinstance(avg_temp, (int, float)):
                    print(f"Sensor {i} Average: {avg_temp:.2f}°C")
                else:
                    print(f"Sensor {i} Average: --°C")  # Fallback for missing values

        time.sleep(5)  # Refresh every 5 seconds