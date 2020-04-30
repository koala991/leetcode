# codind=utf-8

"""
Qucik Sort: 精髓在于第一个while循环, i 停下来的时候, 一定是nums[i] >= x. 若是条件1停下来, 那么上一轮j停下的位置, 原先不满足nums[j] > x, 但是一次交换后就必定有 nums[j] > x, 即此时必然有nums[i] > x, 因此省去两个while循环之后的if判断 nums[i] 与 x 的大小比较
"""

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right):
        if left < right:
            x = nums[right]
            i, j = left, right
            while True:
                while i < j and nums[i] < x:
                    i += 1
                while i < j and nums[j] >= x:
                    j -= 1
                if i == j: break
                self.swap(nums, i, j)

            self.swap(nums, i, right)        
            self.quickSort(nums, left, max(left, i - 1))
            self.quickSort(nums, min(right, i + 1), right)
        return

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        return

if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    print(Solution().sortArray(nums))