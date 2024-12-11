def reocurre(arr): # Brute Force
  min = float("inf")
  min_item = None
  count = 0
  
  for i in range(len(arr)):
    count = 0
    
    for j in range(i+1,len(arr)):
      if arr[i] != arr[j]:
        count += 1
        
      if arr[i] == arr[j] and count < min:
        min = count
        min_item = arr[i]

  return min_item

  # O(n^2)

def reocurre2(arr):
  reocurred_items = {}

  # check if there are more than 1
  if len(arr) < 2:
    return None

  for i in range(len(arr)):
    if arr[i] in reocurred_items: #x in s operator's complexity O(1)
      return arr[i]
    else:
      reocurred_items[arr[i]] = i

  # O(n)

arr = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,4]
arr3 =[2,3,4,5]
print(reocurre2(arr))

    


