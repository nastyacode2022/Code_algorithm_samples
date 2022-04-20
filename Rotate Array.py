"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""




class Solution:

    def rotate(self, nums, k) -> None:

        if k == 0 or len(nums) == k:
            nums
        else:
            for i in range(k):
                a = nums[-1]
                nums.pop()
                nums.reverse()
                nums.append(a)
                nums.reverse()



