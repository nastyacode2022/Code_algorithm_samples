"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
"""




class Solution:
    def maxArea(self, height: List[int]) -> int:

        start_pointer = 0

        end_pointer = len(height) - 1
        area = 0

        while start_pointer < end_pointer:
            breadth = min(height[start_pointer], height[end_pointer])
            length = end_pointer - start_pointer
            area = max(area, (breadth * length))

            if (height[start_pointer] < height[end_pointer]):
                start_pointer += 1
            else:
                end_pointer -= 1
        return area