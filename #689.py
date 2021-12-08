"""
待使用前缀和+滑窗优化
"""
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        self._dp1, self._reverse_dp1 = [None] * n, [None] * n
        self._k, self._n, self._nums = k, n, nums
        max_sum = 0
        ret = None
        for y in range(k, n - k):
            tmp_sum = self.dp1(y - 1)[1] + sum(nums[y: y + k]) + self.reverse_dp1(y + k)[1]
            if tmp_sum > max_sum:
                max_sum = tmp_sum
                ret = (self.dp1(y - 1)[0], y, self.reverse_dp1(y + k)[0])
        return ret

    def reverse_dp1(self, i):
        if self._k + i > self._n:
            return (i, 0)
        elif self._reverse_dp1[i] is not None:
            return self._reverse_dp1[i]
        else:
            sum_i = sum(self._nums[i: i + self._k])
            if sum_i >= self.reverse_dp1(i + 1)[1]:
                self._reverse_dp1[i] = (i, sum_i)
            else:
                self._reverse_dp1[i] = self.reverse_dp1(i + 1)
            return self._reverse_dp1[i]

    def dp1(self, i):
        if i < self._k - 1:
            return (i, 0)
        elif self._dp1[i] is not None:
            return self._dp1[i]
        else:
            sum_i = sum(self._nums[i - self._k + 1: i + 1])
            if sum_i > self.dp1(i - 1)[1]:
                self._dp1[i] = (i - self._k + 1, sum_i)
            else:
                self._dp1[i] = self.dp1(i - 1)
            return self._dp1[i]


if __name__ == "__main__":
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    ans = Solution().maxSumOfThreeSubarrays(nums, k)
    print(ans)
