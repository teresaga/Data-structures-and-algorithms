"""
Best time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def best_time_stock(prices): # O(n) space complexity = O(1)
    min_price = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
        # Update min_price to the lowest price seen so far 
        min_price = min(min_price, prices[i])

        # Calculate profit if we sell in day i
        profit = prices[i] - min_price
        
        # Update max_profit if the profit obtained from the sale on day i is greater
        max_profit = max(max_profit, profit)

        

    return max_profit

arrs = [[7,1,5,3,6,4], [7,6,4,3,1], [1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [3, 1, 4, 8, 7],  [7, 1, 5, 3, 6, 4, 9, 2], [2, 4], [5, 5, 5, 5, 5]]
# Outputs: 5, 0, 6, 0, 7, 8, 2, 0
for arr in arrs:
    print(f" {arr} - Best Profit: {best_time_stock(arr)}")