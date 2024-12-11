def merge_sort(arr): #O(n log n)
    if len(arr) == 1:
        return arr
    
    # split array into 2 parts
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    return merge(
        merge_sort(left), 
        merge_sort(right)
    )

def merge(left, right):
    result = []
    left_index = right_index = 0

    # merge the two halves by compering elements from each half
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    return result + left[left_index:] + right[right_index:] # add the remaining items on one half


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(arr))
