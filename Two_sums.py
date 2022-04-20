"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Test-case:
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        count = 0
        for number in nums:
            count += 1
            for c in range(count, len(nums)):
                if nums[c] + number == target:
                    new_list.append(count - 1)
                    new_list.append(c)
        return new_list