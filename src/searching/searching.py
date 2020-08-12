# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

if start > end:
    return -1

mide = start + (end - start) // 2 # floor 

if target == arr[mid]:
    return mid

elif target < arr[middle]
    return binary_search(arr, target, start, middle-1)

else:
    return binary_search(arr, target, middle +1, end)



def descending_binary_search(arr, target, start, end):
    # descending for agnostic

if start > end:
    return -1

mide = start + (end - start) // 2 # floor 

if target == arr[mid]:
    return mid

elif target < arr[middle]
    # rule out the end side
    return descending_binary_search(arr, target, end, middle-1)

else:
    #rule out the start side
    return descending_binary_search(arr, target, middle +1, start)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):

    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True

    # if array is ascending call binary search
    if is_ascending:
        return binary_search(arr, target, 0, len(arr)-1)
    # otherwise call descending_binary_search
    else:
        return descending_binary_search(arr, target, 0, len(arr)-1)
