"""
1. 快慢指针
2. 二分查找
"""
class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    # def findDuplicate(self, nums) -> int:
    #     """
    #     快慢指针
    #     """
    #     fast, slow = 0, 0
    #     while True:
    #         fast = nums[nums[fast]]
    #         slow = nums[slow]
    #         if fast == slow: break
    #     slow = 0
    #     while True:
    #         fast = nums[fast]
    #         slow = nums[slow]
    #         if fast == slow: break            
    #     return slow

    def findDuplicate(self, nums):
        """
        二分查找
        """
        left, right = 1, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            count = self.countK(nums, mid)
            if count <= mid:
                left = mid + 1
            elif count > mid:
                right = mid
        return left

    def countK(self, nums, k):
        output = 0
        for n in nums:
            if n <= k: output += 1
        return output


        
        
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    print(solution.findDuplicate(nums))