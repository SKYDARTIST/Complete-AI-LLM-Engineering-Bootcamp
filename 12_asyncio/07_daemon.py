import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring Tea Temperature...")
        time.sleep(1)

thread_obj = threading.Thread(target=monitor_tea_temp, daemon=True).start()

print("Main Thread: Making breakfast for 10 seconds...")
time.sleep(4)