# selection_sort.py - selection sort algorithm
#import random
import random

def selection_sort(array):
    sorted_list = []
    while array:
        smallest_index = find_smallest_element_index(array)
        sorted_list.append(array.pop(smallest_index))
    return sorted_list

def find_smallest_element_index(array):
    smallest_index = 0
    for index in range(1, len(array)):
        if array[index] < array[smallest_index]:
            smallest_index = index
    return smallest_index

#arr = [5, 3, 6, 2, 10]
#generate random array with 1 million elements
arr = [random.randint(0, 20000) for _ in range(10000)]
print(selection_sort(arr))