# LeetCode Problem: Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
Problem:
Find the maximum profit from buying and selling a stock.

Approach:
Track the minimum price and compute max profit.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


# Example
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
