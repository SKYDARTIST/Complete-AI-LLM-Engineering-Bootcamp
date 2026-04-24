from multiprocessing import Process
import time


def cpu_heavy_task():
    print("Started cpu heavy task")
    count = 0
    for _ in range(10_000_000):
        count += 1
    print("Finished cpu heavy task")

if __name__ == "__main__":

    start = time.time()

    p1 = Process(target=cpu_heavy_task)
    p2 = Process(target=cpu_heavy_task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time using process is {end-start:.2f} seconds")