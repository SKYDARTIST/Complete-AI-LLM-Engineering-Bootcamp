
# Conceptual

# What's the difference between Process and Thread? When would u pick one over the other?
# Why does multiprocessing bypass the GIL but threading doesn't?
# If each process has its own memory, how would u share data between them?
# Behavioral

# This code takes ~3 seconds total. Why not 9? What would change if u removed the list comprehension and ran them sequentially?
# What happens if u remove if __name__ == "__main__": on Windows vs Mac?
# Why does args need a trailing comma — args=("Chai Maker #1",) — what breaks without it?
# Practical / "what if"

# If brew_chai was doing heavy number crunching instead of time.sleep(), would threading or multiprocessing be faster? Why?
# How would u collect return values from each process? (hint: Process doesn't return values directly — leads to multiprocessing.Queue)
# What's the difference between p.start() + p.join() in two separate loops vs doing both in one loop?



from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")


if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i}", )) for i in range(4)
    ]


    start_time = time.time()
    for p in chai_makers:
        p.start()
    

    for p in chai_makers:
        p.join()

    end_time = time.time()
    print(f"All chai served in {end_time - start_time} seconds")