# codind=utf-8
from typing import List

"""
注意点: 第一次漏掉了 break
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) >> 1
#             if nums[mid] >= target:
#                 right = mid
#             else:
#                 left = mid + 1
#         return left if nums[left] == target else -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    answer = Solution().search(nums, target)
    print(answer)
