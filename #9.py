class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        half = 0
        while half < x:
            x, mod = divmod(x, 10)
            half = half * 10 + mod
        return x == half or x == (half // 10)