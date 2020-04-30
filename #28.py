class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle :
            return 0

        output = -1
        for i in range(0, len(haystack) - len(needle) + 1, 1):
            ii, j = i, 0
            while j < len(needle) and haystack[ii] == needle[j]:
                ii += 1
                j += 1
            if j == len(needle):
                output = i
                break
        return output


        
        