def quick_sort(arr, left, right): # time complexity = O(n log n) ------ space complexity = O(1)
    if left < right:
        pivot_index = partition(arr, left, right)

        # order sublists left and right
        # pivote is already sorted, so it is not included
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)

def partition(arr, left, right):
    # take the last item as pivot
    pivot = arr[right]
    i = left - 1

    # put all items lower than the pivot to the left
    for j in range(left, right):
        if arr[j] <= pivot:
            # take one step to the right
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # the pivot is swap with the item to right of the last item of left partition, so pivote will be right in the middle of two partitions
    arr[i + 1], arr[right] = arr[right], arr[i + 1] 

    # return current position of pivot
    return i + 1

###############################################################################################
###############################################################################################
###############################################################################################

def quick_sort2(arr): # time complexity = O(n log n) ------ space complexity = O(n)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)-1]
        left = []
        right = []

        for i in range(len(arr)-1):
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

        return quick_sort2(left) + [pivot] + quick_sort2(right)



arr = [3,7,8,5,2,1,9,5,4]

quick_sort(arr, 0, len(arr) - 1)
print(arr)

arr2 = [3,7,8,5,2,1,9,5,4]
arr2 = quick_sort2(arr2)
print(arr2)
