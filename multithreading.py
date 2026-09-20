import threading

def task():
    print(threading.current_thread().name, "is Running")

thread1 = threading.Thread(target=task, name="Thread 1")
thread2 = threading.Thread(target=task, name="Thread 2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
