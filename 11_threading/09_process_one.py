import threading
import time


def cpu_heavy_task():
    print("Started cpu heavy task")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("Finished cpu heavy task")



start = time.time()

t1 = threading.Thread(target=cpu_heavy_task)
t2 = threading.Thread(target=cpu_heavy_task)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time using thread is {end-start:.2f} seconds")