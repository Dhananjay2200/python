import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)


time1 = time.perf_counter()
# normal code
# func(4)
# func(2)
# func(1)

# same code using threads
t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[2])
t3 = threading.Thread(target=func,args=[1])
# this task will start after second task will be also start 
t1.start()
t2.start()
t3.start()

# ending of task time
t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()
print(time2-time1)


def poolingdemo():
    with ThreadPoolExecutor() as exe:
        # f1 = exe.submit(func,3)
        # f2 = exe.submit(func,2)
        # f3 = exe.submit(func,4)

        # print(f1.result())
        # print(f2.result())
        # print(f3.result())
        l=[3,5,1,2]
        results = exe.map(func,l)
        for result in results:
            print(result)

poolingdemo()