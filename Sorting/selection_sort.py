def selection_sort(arr): #O(n^2)
    # find the smallest element and swap it whith the first element in the list
    arr_len = len(arr)

    for i in range(arr_len):
        min_value = i # set current index as minimun value
        for j in range(i+1, arr_len):
            if arr[j] < arr[min_value]:
                min_value = j

        arr[i], arr[min_value] = arr[min_value], arr[i]

arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selection_sort(arr)
print(arr)