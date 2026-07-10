class Solution:
    def minSwaps(self, nums):
        k = sum(nums)   # total 1's

        if k <= 1:
            return 0

        nums = nums + nums

        # first window
        ones = sum(nums[:k])
        max_ones = ones

        # sliding window
        for i in range(k, len(nums)):
            ones += nums[i] - nums[i - k]
            max_ones = max(max_ones, ones)

        return k - max_ones