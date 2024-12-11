"""
Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
def climbing_stairs(n): # O(n) space complexity = O(1)
    # base cases
    if n < 2:
        return n
    
    # save previous two cases
    prev1 = 1
    prev2 = 2

    for _ in range(3,n+1):
        temp = prev1 + prev2
        prev1 = prev2
        prev2 = temp

    return prev2

calculations = 0
def memoization_climbing_stairs():
    cache = {}
    
    def climbing_stairs_recursive(n):
        global calculations
        calculations += 1
        if n in cache:
            return cache[n]
        if n <= 2:
            return n
        
        cache[n] = climbing_stairs_recursive(n-1) + climbing_stairs_recursive(n-2)
        
        return cache[n]
    
    return climbing_stairs_recursive

print(climbing_stairs(5))

memo_climbing_stairs = memoization_climbing_stairs()
print(memo_climbing_stairs(5))
print(calculations)