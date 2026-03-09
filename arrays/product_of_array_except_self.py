# LeetCode Problem: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

"""
Problem:
Return an array where each element is the product of all other elements.

Approach:
Use prefix and suffix products.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# Example
nums = [1,2,3,4]
print(productExceptSelf(nums))

