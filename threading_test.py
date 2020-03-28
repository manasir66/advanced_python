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

#we can have more than one thread and we can also synchrnoize multiple threads
#that are accesing a global variable to print out a final value in the main thread

# the thread.join() command tells python to wait till that thread is done before moving to the next line
#make a global list
ls = []
def count_1(n):
  for i in range(1, n+1):
    ls.append(i)
    time.sleep(0.5)

def count_2(n):
  for i in range(1, n+1):
    ls.append(i**3)
    time.sleep(0.5)

x_t1 = threading.Thread(target=count_1, args=(5,)) #thread 1
x_t1.start()

y_t2 = threading.Thread(target=count_2, args=(5,)) #thread 2
y_t2.start()

print("Number of active threads : ", threading.activeCount()) 

x_t1.join()
y_t2.join()

print(ls)



