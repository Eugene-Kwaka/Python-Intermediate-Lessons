from threading import Thread, Lock
import time

################ SHARING DATA IN THREADS ###############
        
# Global value to simulate a database
database_value = 0

# increase method
def increase(lock):
    # To modify the global database value:
    # I want to simulate some database access, get database value and copy it in a local database
    global database_value
    
    # Using Lock as a context manager
    # Using it this way will automatically run the acquire() method to enable locked state and release() method for the unlocked state
    with lock:
        local_copy = database_value
        # processing
        # Changing the value of local_copy to a new one
        local_copy += 1
        # Since we have three threads, the python interpreter has a waiting time(0.1 seconds) for it to switch from one thread to another one.
        # All threads carryout the increase function; changing the value of the database from 0 to 1.
        # This lock handles race condition to enable synchronization of the threads sharing the same resource to run concurrently avoiding errors.
        time.sleep(0.1)
        # Write new value back to database_value
        database_value = local_copy
    
        

if __name__=="__main__":
    
    # Declaring lock
    lock = Lock()
    
    print("Start Value", database_value)
    
    # Create threads
    # the lock is used as an argument for the increase function as stated above
    thread1 = Thread(target=increase, args=(lock, ))
    thread2 = Thread(target=increase, args=(lock, ))
    thread3 = Thread(target=increase, args=(lock, ))
    
    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()
    
    # Waiting for the threads to finish executing
    thread1.join()
    thread2.join()
    thread3.join()
    
    print("End value", database_value)
    
    print("End main")
     
     
        
   