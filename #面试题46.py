# class Solution:
#     def translateNum(self, num: int) -> int:
#         self.cache = {}
#         self.count = 0
#         if num
        
#     def _translateNumI(self, num, i):
#         if i in self.cache:
#             self.count += 1
#             return self.cache[i]
#         if i >= len(nums):
#             retrun 0
#         elif i >= len(nums) - 2:
#             return 
            
            
#         output = 0
#         if i in self.cache:
#             output = self.cache[i]
#         else:
#             output = self._translateNumI(num, i + 1)
#             if int(num[i:]) < 26: output += self._translateNumI(num, i + 1)
        
        
"""dp(i) = dp(i + 1) + dp(i + 2) * I(9 < int(num[i: i + 2]) < 26)"""
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        plus_1, plus_2 = 1, 0
        for i in range(len(num) - 1, -1, -1):
            curr = plus_1
            if 9 < int(num[i: i + 2]) < 26: curr += plus_2
            plus_1, plus_2 = curr, plus_1
        return plus_1

# if __name__ == "__main__":
#     solution = Solution()
#     num = 12258
#     print(solution.translateNum(12258))