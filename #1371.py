class Solution:
    vowels = ["a", "e", "i", "o", "u"]
    
    def findTheLongestSubstring(self, s: str) -> int:
        status = {v: 0 for v in self.vowels}
        max_len = 0
        debut = {self.getStatusCode(status): -1}
        for i in range(len(s)):
            if s[i] in status:
                status[s[i]] ^= 1
            code = self.getStatusCode(status)
            if code in debut:
                max_len = max(i - debut[code], max_len)
            else:
                debut[code] = i
        return max_len            

    def getStatusCode(self, status):
        code = 0 
        for i, v in enumerate(self.vowels):
            code += 2 ** i * status.get(v, 0)
        return code



