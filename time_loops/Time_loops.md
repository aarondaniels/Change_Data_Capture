# What Are Time Loops?

Time loops are used to schedule when you want an action or a function to be performed. This functionality is useful for implementing the running of simple code and functions, as well as some more complex functionalities involving applications development, CDC, etc. In other words, time loops can also be used to represent actions that need to be scheduled to run after a certain amount of time.

# How Can Time Loops Be Implemented in Python?

The easiest way to implement time loops in Python is by using the timer()method from the library threading.

Note that you must install the library using the following syntax in your Terminal window:

`pip3 install pip3 install thread6`

The method has the following general syntax:

`threading.Timer(interval, your_function)`

where interval is the time, in seconds, after you want your function to run, and your_function is the name of the function you want to invoke after the predetermined amount of time.

To create a timer that will run your function `pcde()` that prints the string `“This is a time loop demo.”` after five seconds, you would write the following syntax:

``` python
import threading

def pcde():

   print(“This is a course in data engineering.”)

timer = threading.Timer(5.0, pcde)

timer.start()

print("Exit\n")
```

The output of the code above will be:


`Exit`

`This is a time looop demo.`

where the last string gets printed five seconds after the string “Exit”.

To cancel a timer, you will need to use the following syntax:

``` python
timer.cancel()
```

The function above will stop the timer and cancel the execution of the timer’s action. This will only work if the timer is still in its running or waiting stage.

Observe the following syntax:


``` python
import threading

from threading import Timer

def pcde():

   print(“This is time loop demo”)

timer = threading.Timer(5.0, pcde)

timer.start()

print(“Cancelling timer\n”)

timer.cancel()

print("Exit\n")
```

The output of the above syntax will be:

`Cancelling timer`

`Exit`

because the timer has been cancelled while it was still in a waiting stage. The two strings will be printed at the same time.