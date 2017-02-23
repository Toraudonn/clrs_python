from matplotlib import pyplot as plt
import numpy as np
import scipy as sci

import time as t

# Big-O notation explained by a self-taught programmer:
# https://justin.abrah.ms/computer-science/big-o-notation-explained.html

# algorithm

num_list = [5, 16, 2, 3, 10, 7, 1, 4, 4]

best_case = [1,2,3,4,4,5,7,10,16]
worst_case = [16,10,7,5,4,4,3,2,1]

# insertion sort
def insertion(l):
    for i in range(1, len(l)):
        j = i 
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j = j - 1
    return l

start = t.time()
insertion(best_case)
some_time = t.time() - start
print("-------------- best case: %s seconds ---------------" % some_time)

start = t.time()
insertion(worst_case)
some_time = t.time() - start
print("-------------- worst case: %s seconds ---------------" % some_time)
