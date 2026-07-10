class Solution:
    def sumOfUnique(self, nums):
        freq = {}

        # count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # sum unique elements
        total = 0
        for num in freq:
            if freq[num] == 1:
                total += num

        return total
        