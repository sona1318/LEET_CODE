class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2 #calculate nos. from 1 to n
        k = n // m  #how many nos. divisible by m
        num2 = m * k * (k + 1) // 2
        return total - 2 * num2