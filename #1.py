# codind=utf-8
"""Two Sum"""


# class Solution:
#     def twoSum(self, nums, target):
#         count = 0
#         while nums:
#             x = nums.pop(0)
#             count += 1
#             if target - x in nums:
#                 return [count - 1, nums.index(target - x) + count]
#         return -1

class Solution:
    def twoSum(self, nums, target):
        ever = {}
        for i, x in enumerate(nums):
            if target - x in ever:
                return [ever[target - x], i]
            elif x not in ever:
                ever[x] = i
        else:
            return -1

if __name__=="__main__":
    nums = [3, 2, 4]
    print(Solution().twoSum(nums, 6))



