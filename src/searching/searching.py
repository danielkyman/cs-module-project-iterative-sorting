# def linear_search(arr, target):
#     # Your code here

#     for i in range(len(arr)):
#         if target is arr[i]:

#     return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) is 0:
        return -1
    if arr[0] is target:
        return 0

    startIndex = 0
    endIndex = len(arr) - 1

    while startIndex < endIndex:
        middleIndex = int((endIndex - startIndex) / 2)
        if target is arr[middleIndex]:
            return middleIndex
        elif target < arr[middleIndex]:
            endIndex = middleIndex - 1
        else:
            startIndex = middleIndex + 1

    if arr[startIndex] is target:
        return startIndex

    return -1  # not found
