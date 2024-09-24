import threading
import time

def simulate_io_task(file_name, duration):
    print(f"Starting to download {file_name}...")
    time.sleep(duration)
    print(f"Finished downloading {file_name}!")

def run_io_tasks():
    files_to_download = ["numbers.txt", "numbers1.txt", "numbers2.txt", "numbers3.txt"]
    threads = []

    for file in files_to_download:
        thread = threading.Thread(target=simulate_io_task, args=(file, 5))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

