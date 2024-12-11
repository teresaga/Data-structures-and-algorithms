def find_factorial_recursive(num): # O(n)
  if num == 1:
    return 1
    
  return num * find_factorial_recursive(num - 1)

def find_factorial_iterative(num): # O(n)
  if num == 1:
    return 1
    
  factorial = 1
  for i in range(2, num + 1):
    factorial *= i

  return factorial

print(find_factorial_iterative(5))
print(find_factorial_recursive(5))

# Given a number N return the index value of the Fibonacci sequence:
# 0 1 1 2 3 5 8 13 21 34 55
def find_fibonacci_recursive(n): # O(2^n)
  if n < 2:
    return n
  else:
    return find_fibonacci_recursive(n-1) + find_fibonacci_recursive(n-2)


  
def find_fibonacci_iterative(n): # O(n)
  arr = [0, 1]
  for i in range(2, n+1):
    arr.append(arr[i-1] + arr[i-2])

  return arr[n]

print(find_fibonacci_iterative(8))
print(find_fibonacci_recursive(8))

def reverse_string(str):
  str_list = list(str)
  i=0
  j= len(str) - 1
  
  while True:
    if j <= i:
      return "".join(str_list)
      
    str_list[i], str_list[j] = str_list[j], str_list[i]

    i += 1
    j -= 1
  

print(reverse_string("yoyo master"))

def reverse_string_recursive(str):
  if str == "":
    return ""
  else:
    return reverse_string_recursive(str[1::]) + str[::1]

reverse_string_recursive("yoyo master")