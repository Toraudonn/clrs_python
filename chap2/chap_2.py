import time as t

# Loop Invariant:

# Initialization: It is true prior to the first iteration of the loop.
# Maintenance: If it is true before an iteration of the loop, it remains true before the next iteration.
# Termination: When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct.

num_list = [5, 16, 2, 3, 10, 7, 1, 4, 4]

best_case = [1,2,3,4,4,5,7,10,16]
worst_case = [16,10,7,5,4,4,3,2,1]

# Selection-sort

def selection(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if(l[i]>l[j]):
                l[i], l[j] = l[j], l[i]
    return l

print(selection(num_list))