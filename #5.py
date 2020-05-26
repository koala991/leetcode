# codind=utf-8

"""
中心外推法, 对每个字符, 有作为中心(奇数长度回文) 和作为中心偏左字符(偶数长度回文) 的可能性.
问题: 循环结束后, _j 需要 -1 才是真实停止的长度, 不够优雅
"""

# class Solution:
#     # def longestPalindrome(self, s: str) -> str:
#     def longestPalindrome(self, s):
#         max_length = 0
#         longest = ""
#         for _i in range(len(s)):
#             _j = 0
#             while (
#                 _i - _j >= 0 
#                 and _i + _j < len(s)
#                 and s[_i - _j] == s[_i + _j]):
#                 _j += 1
#             _j -= 1
#             if _j * 2 + 1 > max_length:
#                 longest = s[(_i - _j): (_i + _j + 1)]
#                 max_length = _j * 2 + 1 
#             _j = 1
#             while (
#                 _i - _j + 1 >= 0
#                 and _i + _j < len(s)
#                 and s[_i - _j + 1] == s[_i + _j] ):
#                 _j += 1
#             _j -= 1
#             if _j * 2 > max_length:
#                 longest = s[(_i - _j + 1): (_i + _j + 1)]
#                 max_length = _j * 2
#         return longest


class Solution:
    hist = {}
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s):
        # if len(s) == 0:
        #     return ""
        longest = ""
        self.str_len = len(s)
        i, target_len = 0, self.str_len
        while target_len > 0:
            if self.isPalindrome(s, i, i + target_len - 1):
                longest = s[i: i + target_len]
                break
            elif (i + target_len) == self.str_len:
                i = 0
                target_len -= 1
            else:
                i += 1
        return longest

    def isPalindrome(self, in_s, i, j):
        index = i * self.str_len + j
        output = True
        if i >= j:
            pass
        elif index in self.hist:
            output = self.hist[index]
        else:
            output = in_s[i] == in_s[j] and self.isPalindrome(in_s, i + 1, j - 1)
            self.hist[index - self.str_len - 1] = output
        return output          



if __name__ == "__main__":
    # s = "babad"
    # s = "cbbc"
    s = "cbbd"
    answer = Solution().longestPalindrome(s)
    print(answer)
