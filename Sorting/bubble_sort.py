arr = [6, 5, 3, 1, 8, 7, 2, 4]

def bubble_sort(arr): #O(n^2)
    i = 0
    j = len(arr)-1

    while j > 0:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        
        i += 1

        if j == i:
            i = 0
            j -= 1
    
def bubble_sort2(arr): #O(n^2)
    arr_len = len(arr)

    for i in range(arr_len):
        swapped_items = False
        for j in range(arr_len - i -1): # the lastest numbers are already sorted, so there is no need to check them in the next iteration
            if j+1 >= arr_len:
                break

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped_items = True

        if not swapped_items: # If there was no swap, they are already sorted
            break

bubble_sort2(arr)
print(arr)