"""非动态规划，考虑前缀乘积的解法。 时间复杂度O(n) 空间复杂度 O(1)"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_product = nums[0]
        i = 0
        while i < len(nums):
            cumprod, cumneg_prod = 1, 1
            for j in range(i, len(nums), 1):
                cumprod *= nums[j]
                if cumprod >= 0:
                    max_product = max(cumprod, max_product)
                    if cumprod == 0:
                        i = j + 1
                        break                    
                elif cumprod < 0:
                    max_product = max(cumprod // cumneg_prod, max_product) # all is int so equals /
                    cumneg_prod = cumprod if cumneg_prod > 0 else cumneg_prod
            else:
                break
        return max_product


