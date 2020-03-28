#Threading is the idea of switching between threads in a single core
#Single core cpus can have multiple threads that are concurrently running
#concurrency is not parallelism but rather executing in different time frames

import threading
import time

#to make a thread you need to make a function that acts as a thread

#after defining a function we can create a variable and assign the threading module to it by passing the newly created function as the target (this is all syntax)

def func_to_thread():
  print("some randome string")
  time.sleep(5)
  print("done printing the string")


my_new_thread = threading.Thread(target=func_to_thread) 

#pass the name of the function only 
#we also have to define args= and pass a tuple value if our function takes in arguments

#to run a thread we have to use thread.start()

my_new_thread.start() #starts the thread

print("Number of active threads : ", threading.activeCount())

#the number of active threads will be displayed while the thread 1 is asleep

