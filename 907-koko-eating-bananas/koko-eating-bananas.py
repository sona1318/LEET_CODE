import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                right = mid   # try smaller k
            else:
                left = mid + 1  # need bigger k

        return left
        