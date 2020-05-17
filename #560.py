class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    def subarraySum(self, nums, k):
        output = 0
        pre_sum, his_sum = 0, {}
        for num in nums:
            pre_sum += num
            output += his_sum.get(pre_sum - k, 0) + int(pre_sum == k)
            his_sum[pre_sum] = his_sum.get(pre_sum, 0) + 1
        return output

if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))
