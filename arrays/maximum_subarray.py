# LeetCode Problem: Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

"""
Problem:
Find the contiguous subarray with the largest sum.

Approach:
Kadane's Algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
