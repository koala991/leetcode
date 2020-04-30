# codind=utf-8
"""Two Sum"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = [-1, -1]
        reverse_map = dict()
        for i, x in enumerate(nums):
            if x in reverse_map:
                output[0], output[1] = reverse_map[x], i 
            else:
                reverse_map[target - x] = i
        return output

if __name__=="__main__":
    nums = [3, 2, 4]
    print(Solution().twoSum(nums, 6))



