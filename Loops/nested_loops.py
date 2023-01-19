# Outer Loop
for i in range(10):
    # inner loop
    for j in range(10):
        print(0, end=" ")
    print()
    
# For ever iteration of the outer loop, the inner loop will be executed 10 times(range).
# This will print a 2D array of 0s since the outer loop was executed 10 times while the inner loop was executed 10 inside it. 
# The outer loop must run before it then the inner loops runs before the iteration returns back to the outer loop for it to run again.

# Forloop iteration increases time complexity if a given dataset to interate to is very large. 
# I can calculate the total time complexity by importing time. 

import time

start_time  = time.time()
# Outer Loop
for i in range(10):
    # inner loop
    for j in range(10000):
        print(0, end=" ")
    print()
    
# Time taken to run the loop equals to total_time_taken - start_time
print(round((time.time() - start_time), 2)) #In this case, it took 0.4 sseconds to run the loop. This can increase dramatically if the dataset is very large. 