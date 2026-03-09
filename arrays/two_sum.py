# LeetCode Problem: Two Sum
# https://leetcode.com/problems/two-sum/

"""
Problem:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Approach:
Use a hashmap to store numbers and their indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i

    return []


# Example test
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
