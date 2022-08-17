import time
from threading import Timer

def task1():
    print('Task 01') #define dummy tasks
    time.sleep(2) #sleep for a couple of seconds to simulate processing time

def task2():
    print('Task 02') #dummy task two
    time.sleep(3) #simulate processing time

def timeloop():
    task1()
    task2()
    print(f'--- LOOP: ' + time.ctime() + ' ---')
    Timer(5, timeloop).start()

timeloop()