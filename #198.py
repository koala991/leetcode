"""动态规划, 循环实现"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_i, max_pre1, max_pre2 = 0, 0, 0
        for i in range(len(nums)):
            max_i = max(max_pre1, max_pre2 + nums[i])
            max_pre2 = max_pre1
            max_pre1 = max_i
        return max_i
