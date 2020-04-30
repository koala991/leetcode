class Solution:
    # def reversePairs(self, nums: List[int]) -> int:
    def reversePairs(self, nums):
        if len(nums) == 0:
            return 0
        s_nums, output = [], 0
        s_nums.append(nums.pop(0))
        while len(nums) > 0:
            x = nums.pop(0)
            index = self.searchInsertIndex(s_nums, x)
            output += len(s_nums) - index
            s_nums.insert(index, x)
        return output

    def searchInsertIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            elif nums[mid] > target:
                right = mid
        if nums[left] <= target < nums[right]:
            output =  left + 1
        elif nums[left] > target:
            output = left # 0
        elif nums[right] <= target:
            output = right + 1 # len(nums) - 1
        return output


if __name__ == "__main__":
    nums = [7,5,6,4]
    print(Solution().reversePairs(nums))