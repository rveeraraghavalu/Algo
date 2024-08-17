# Binary Search Algorithm
def bin_search(arr, target):
# Initialize starting point and end point
    low = 0
    # Initialize end point
    high = len(arr) - 1
    # Loop until low is less than or equal to high
    while low <= high:
        # Find the middle point
        mid = (low + high) // 2
        # Compare the middle point with the target
        if arr[mid] == target:
            # Return the middle point
            return mid
        # If the target is less than the middle point
        elif arr[mid] < target:
            # Update the low point
            low = mid + 1
        # If the target is greater than the middle point
        else:
            # Update the high point
            high = mid - 1
    return -1 

def test_bin_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    target = 5
    assert bin_search(arr, target) == 4

    target = 21
    assert bin_search(arr, target) == -1

    target = 0
    assert bin_search(arr, target) == -1

    target = 20
    assert bin_search(arr, target) == 19

    print("All test cases passed!")

test_bin_search()


