# codind=utf-8

"""
注意点: 第一次漏掉了 break
"""

class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        output = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                output = mid
                break
        return output


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    answer = Solution().search(nums, target)
    # assert answer == "bb"
    print(answer)
