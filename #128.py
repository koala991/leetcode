class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # def longestConsecutive(self, nums) -> int:
        nums = set(nums)
        head_info, tail_info = {}, {}
        for n in nums:
            pre_len = tail_info.get(n - 1, 0)
            after_len = head_info.get(n + 1, 0)
            if pre_len == 0 and after_len == 0:
                head_info.setdefault(n, 1)
                tail_info.setdefault(n, 1)
            elif pre_len > 0 and after_len == 0:
                tail_info.pop(n - 1)
                tail_info[n] = pre_len + 1
                head_info[n - pre_len] = pre_len + 1
            elif pre_len == 0 and after_len > 0:
                head_info.pop(n + 1)
                head_info[n] = after_len + 1
                tail_info[n + after_len] = after_len + 1
            elif pre_len > 0 and after_len > 0:
                head_info.pop(n + 1)
                tail_info.pop(n - 1)
                head_info[n - pre_len] = pre_len + 1 + after_len
                tail_info[n + after_len] = pre_len + 1 + after_len
            
        max_len = 0
        for v in head_info.values():
            max_len = max(max_len, v)

        return max_len




# if __name__ == "__main__":
#     solution = Solution()
#     nums = [100,4,200,1,3,2]
#     print(solution.longestConsecutive(nums))
