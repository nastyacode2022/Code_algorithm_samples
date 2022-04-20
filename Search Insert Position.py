"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""




class Solution:

    def searchInsert(self, nums, target) -> int:

        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            for j in range(len(nums)):
                if nums[j] > target:
                    return j
                elif j == int(len(nums)) - 1 and nums[j] < target:
                    return j + 1