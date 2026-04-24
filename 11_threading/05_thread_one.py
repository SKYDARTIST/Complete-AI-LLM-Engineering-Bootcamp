import threading
import time

def boil_milk():
    print(f"Started boiling milk...")
    time.sleep(2)
    print(f"Finished boiling milk...")


def toast_bread():
    print(f"Started toasting bread...")
    time.sleep(3)
    print(f"Finished toasting bread...")


start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bread)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Total time using thread is {end-start:.2f} seconds")