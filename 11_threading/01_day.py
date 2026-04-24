
# Conceptual

# What is a thread, and why would u use two instead of running these functions one after the other?

# What's the difference between start() and join()? What happens if u remove the join() calls?

# Why does the output interleave (order #1, brew #1, order #2...) instead of finishing take_orders completely before starting brew_chai?

# Behavioral

# How long does this program take to run total — and why is it NOT 2+2+2+3+3+3 = 15 seconds?

# What would happen if u called order_thread.join() before brew_thread.start()?

# Is this code using parallelism or concurrency? What's the difference?

# Practical / "what if"

# What if both threads try to write to the same variable — what goes wrong? (leads to race conditions)

# How would u pass arguments to take_orders if it needed a name parameter?

# What's the Python GIL, and why does it mean threads here don't actually run simultaneously on multiple CPU cores?

# The core insight this code teaches:

# time.sleep() represents I/O wait (like a network call or DB query). Threading shines here because while one thread is "waiting," the other runs. That's the whole point — not speed, but not blocking.

# The GIL question is the trap one — worth knowing cold if u're going for any Python backend role.




import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(1)


def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)

#create threads

order_thread = threading.Thread(target = take_orders)
brew_thread = threading.Thread(target = brew_chai)

order_thread.start()
brew_thread.start()


order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")