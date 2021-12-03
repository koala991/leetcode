"""
题目中限制了nums中元素的范围，在这个条件下，使用基数排序是更好的方案。
"""

from typing import List 
import heapq


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        max_sum, min_abs = 0, abs(nums[0])
        neg_nums = []
        while len(nums) > 0:
            num = nums.pop()
            if num < 0:
                heapq.heappush(neg_nums, num)
            min_abs = min(min_abs, abs(num))
            max_sum += num
        while len(neg_nums) > 0 and k > 0:
            num = heapq.heappop(neg_nums)
            max_sum -= 2 * num
            k -= 1
        if k > 0:
            max_sum -= (k % 2) * min_abs * 2
        return max_sum
        

if __name__ == "__main__":
    nums, k = [4,2,3], 1
    ans = Solution().largestSumAfterKNegations(nums, k)
    print(ans)
