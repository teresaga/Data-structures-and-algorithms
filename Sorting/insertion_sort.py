def insertion_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len):
        current_value = arr[i]
        j = i - 1

        # Shift the values ​​to the right until find the correct place for the current value
        while j >= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current_value


            

arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertion_sort(arr)
print(arr)