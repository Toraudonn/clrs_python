import time as t

num_list = [5, 16, 2, 3, 10, 7, 1, 4, 4]

best_case = [1,2,3,4,4,5,7,10,16]
worst_case = [16,10,7,5,4,4,3,2,1]

# merge sort
def merge(l):
    if(len(l)>1):
        mid = len(l)//2
        left, right = l[:mid], l[mid:]
        
        # recursive...
        merge(left)
        merge(right)
        
        i=j=k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k]=left[i]
                i=i+1
            else:
                l[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            l[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            l[k]=right[j]
            j=j+1
            k=k+1
        
    return l

start = t.time()
merge(best_case)
some_time = t.time() - start
print("-------------- best case: %s seconds ---------------" % some_time)

start = t.time()
merge(worst_case)
some_time = t.time() - start
print("-------------- worst case: %s seconds ---------------" % some_time)
