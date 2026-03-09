# LeetCode Problem: Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

"""
Problem:
Given an integer array nums, return True if any value appears at least twice.

Approach:
Use a set to track seen numbers.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Example
nums = [1,2,3,1]
print(containsDuplicate(nums))
