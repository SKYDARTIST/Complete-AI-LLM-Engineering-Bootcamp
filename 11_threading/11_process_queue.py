from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Hot Chai is ready ☕")

if __name__ == "__main__":

    queue = Queue()


    process = Process(target=prepare_chai, args=(queue,))

    process.start()

    print("Taking Chai", queue.get())

    process.join()