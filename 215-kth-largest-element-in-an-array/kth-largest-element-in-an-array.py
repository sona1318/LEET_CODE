import random

class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k

        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]

            low, mid, high = l, l, r

            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:
                    mid += 1

            if target < low:
                return quickselect(l, low - 1)
            elif target > high:
                return quickselect(high + 1, r)
            else:
                return nums[target]

        return quickselect(0, len(nums) - 1)