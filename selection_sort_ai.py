#write a function to do selection sort
import random
def selection_sort(array):
    sorted_list = []
    while array:
        smallest_index = find_smallest_element_index(array)
        sorted_list.append(array.pop(smallest_index))
    return sorted_list 

#write a function to find the smallest element index
def find_smallest_element_index(array):
    smallest_index = 0
    for index in range(1, len(array)):
        if array[index] < array[smallest_index]:
            smallest_index = index
    return smallest_index


#arr = [5, 3, 6, 2, 10]
#generate random array with 1 million elements
#arr = [random.randint(0, 20000) for _ in range(20000)]
#print(selection_sort(arr)) 

#write test case for selection sort
def test_selection_sort():
    assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]

    assert selection_sort([10, 5, 2, 3]) == [2, 3, 5, 10]

    assert selection_sort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    print("All test cases passed!")     


test_selection_sort()

