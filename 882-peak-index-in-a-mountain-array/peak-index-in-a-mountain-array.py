class Solution:
    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1   # go right
            else:
                right = mid      # go left

        return left
        