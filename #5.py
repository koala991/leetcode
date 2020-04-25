# codind=utf-8

"""
中心外推法, 对每个字符, 有作为中心(奇数长度回文) 和作为中心偏左字符(偶数长度回文) 的可能性.
问题: 循环结束后, _j 需要 -1 才是真实停止的长度, 不够优雅
心得: 初始化要好好考虑, 遇到两个这样问题.
"""

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s):
        max_length = 0
        longest = ""
        for _i in range(len(s)):
            _j = 0
            while (
                _i - _j >= 0 
                and _i + _j < len(s)
                and s[_i - _j] == s[_i + _j]):
                _j += 1
            _j -= 1
            if _j * 2 + 1 > max_length:
                longest = s[(_i - _j): (_i + _j + 1)]
                max_length = _j * 2 + 1 
            _j = 1
            while (
                _i - _j + 1 >= 0
                and _i + _j < len(s)
                and s[_i - _j + 1] == s[_i + _j] ):
                _j += 1
            _j -= 1
            if _j * 2 > max_length:
                longest = s[(_i - _j + 1): (_i + _j + 1)]
                max_length = _j * 2
        return longest

if __name__ == "__main__":
    # s = "babad"
    # answer = Solution().longestPalindrome(s)
    # # assert answer == "bab"
    # print(answer)

    s = "cbbd"
    answer = Solution().longestPalindrome(s)
    # assert answer == "bb"
    print(answer)

