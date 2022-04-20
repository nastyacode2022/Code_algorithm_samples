"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
Input: n = 1
Output: true
Explanation: 20 = 1
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = 1
        if n==1:
            return True
        else:
            while 2**m<=n:
                if n==1:
                    return True
                elif 2**m == n:
                    return True
                else:
                    m+=1