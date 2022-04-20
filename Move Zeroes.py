"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[i],nums[p] = nums[p],nums[i]
                p+=1