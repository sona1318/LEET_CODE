class Solution:
    def shipWithinDays(self, weights, days):
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            required_days = 1
            current = 0

            for w in weights:
                if current + w > mid:
                    required_days += 1
                    current = 0
                current += w

            if required_days <= days:
                right = mid   # try smaller capacity
            else:
                left = mid + 1  # need bigger capacity

        return left
        