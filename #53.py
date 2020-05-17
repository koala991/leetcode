"""
分治法待实现
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_sum = nums[0]
        before_sum = 0
        for x in nums:
            tmp_arrsum = x + before_sum
            max_sum = tmp_arrsum if tmp_arrsum > max_sum else max_sum
            before_sum = 0 if tmp_arrsum < 0 else tmp_arrsum
        return max_sum
        