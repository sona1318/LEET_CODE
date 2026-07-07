# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid   # first bad is at mid or before
            else:
                left = mid + 1  # first bad is after mid
        
        return left