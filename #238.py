class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        cum_prod = 1
        for i in range(n):
            output[i] *= cum_prod
            cum_prod *= nums[i]

        cum_prod = 1
        for i in range(n - 1, -1, -1):
            output[i] *= cum_prod
            cum_prod *= nums[i]

        return output