"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""



class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new_tuple = sorted(tuple(nums1) + tuple(nums2))
        if len(new_tuple) % 2 != 0:
            return float(new_tuple[int((len(new_tuple)) / 2 - 0.5)])
        else:
            return (new_tuple[int((len(new_tuple)) / 2 - 1)] + new_tuple[int((len(new_tuple)) / 2)]) / 2