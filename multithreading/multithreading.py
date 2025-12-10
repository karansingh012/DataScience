## Multithreading 
## When to use multithreading
## I/O bound task: tasks that spend more time waiting for I/O operations(e.g, file operation,network request).
## Concurrent Execution: When you want to improve the throughput of your application by performing multiple operations concurrently

import threading
import time 
def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")

t = time.time()
print_number()
print_letter()
finished_time = time.time()-t
print(finished_time)

