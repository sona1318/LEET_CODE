class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1 #left starts at the begining(index 0), right start ath the end(last index)
        while left < right: #continue swapping until two pointers cross each other
            s[left], s[right] = s[right], s[left] #swap the first and alst element
            left += 1  #move left forward
            right -= 1   #move right backward
       