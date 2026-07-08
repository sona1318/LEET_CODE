class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0  #stop when it become 0
        while num > 0:
            if num % 2 == 0: #if number is even % 2
                num //= 2   #to remove decimal number
            else:
                num -= 1    #if num is even -1
            steps += 1 #to know how many steps used
        return steps