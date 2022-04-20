"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""



class Solution:
    def search(self, nums, target) -> int:
        number = 0
        for i in range(len(nums)):
            if nums[i] == target:
                number += i
                return number
        if number == 0:
            return '-1'
        else:
            return number