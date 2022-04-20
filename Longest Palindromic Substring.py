"""
Given a string s, return the longest palindromic substring in s.
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxLenStart = 0
        maxLenEnd = 0

        def checkSubstr(l, r):
            nonlocal maxLen
            nonlocal maxLenStart
            nonlocal maxLenEnd

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxLenStart = l
                    maxLenEnd = r + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd substr
            checkSubstr(i, i)
            # even substr
            checkSubstr(i, i + 1)

        return s[maxLenStart:maxLenEnd]