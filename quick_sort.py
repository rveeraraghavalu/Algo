#quick sort algorithm
import random
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [ i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
#print(quick_sort([10, 5, 2, 3]))
arr = [random.randint(0, 1000) for _ in range(1000)]
print(quick_sort(arr))