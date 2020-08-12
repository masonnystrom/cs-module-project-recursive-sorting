# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # merged_arr = [0] * elements

    merged_arr = []
    
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0:
        merged_arr += arrB
    else:
        merged_arr += arrA
    return merged_arr

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        mid = len(arr) //2
        a = merge_sort(arr[:mid])
        b = merge_sort(arr[mid:])
        return merge(a,b)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

