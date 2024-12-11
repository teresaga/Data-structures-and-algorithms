# Given a number N return the index value of the Fibonacci sequence:
# 0 1 1 2 3 5 8 13 21 34 55
calculations = 0
def find_fibonacci_recursive(n): # O(2^n)
  global calculations
  calculations += 1
  if n < 2:
    return n
  else:
    return find_fibonacci_recursive(n-1) + find_fibonacci_recursive(n-2)

calculations2 = 0
# Dynamic programmic and closure
def memoized_fibonacci(): # O(n)
    solutions = {}
    def fib(n):
        global calculations2
        calculations2 += 1
        if n in solutions:
            return solutions[n]
        else:
            if n < 2:
                return n
            else:
                solutions[n] = fib(n-1) + fib(n-2)
                return solutions[n]
    return fib

calculations3 = 0
# Dinamic programmic without closure
def simple_fib(n, solutions={}):
    global calculations3
    calculations3 += 1
    if n in solutions:
        return solutions[n]
    else:
        if n < 2:
            return n
        else:
            solutions[n] = simple_fib(n-1) + simple_fib(n-2)
            return solutions[n]
            



print(find_fibonacci_recursive(7))
print(f"fibonacci calculations: {calculations}")

fibonacci = memoized_fibonacci()
print(fibonacci(7))
print(f"fibonacci calculations: {calculations2}")

print(simple_fib(7))
print(f"fibonacci calculations: {calculations3}")