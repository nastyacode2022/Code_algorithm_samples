"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        res=-1
        while l<=r:
            mid=(l+r)//2
            ans=isBadVersion(mid)
            if ans == False:
                l=mid+1
            else:
                res=mid
                r=mid-1
        return res