class Solution:
    def validPalindrome(self, s: str) -> bool:
        output = True
        l, r = 0, len(s) - 1
        n_mismatch = 0
        while l < r:
            if s[l] != s[r]:
                break                                
            l += 1
            r -= 1

        if l < r:
            output = self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
        return output

    def isPalindrome(self, s, i, j):
        output = True
        while i <= j:
            if s[i] != s[j]:
                output = False 
                break
            i += 1
            j -= 1
        return output