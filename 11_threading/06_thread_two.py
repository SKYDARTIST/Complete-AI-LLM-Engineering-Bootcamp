import threading
import time


def prepare_chai(type_, wait_time):
    print(f"Started preparing {type_} chai...")
    time.sleep(wait_time)
    print(f"Finished preparing {type_} chai...")


t1 = threading.Thread(target=prepare_chai, args=("Masala", 3))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 4))

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time for chai using thread is {end-start:.2f} seconds")