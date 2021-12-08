class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        i = 0
        while k > 0 and i < len(s):
            if s[i] == " ":
                k -= 1
            i += 1
        return s[:i - 1 if k == 0  else i]
