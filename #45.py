class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        n_steps = 0
        i = 0
        while True:
            if i + nums[i] >= len(nums) - 1: 
                n_steps += 1
                break
            next_i = i
            for j in range(i + 1, i + nums[i] + 1, 1):
                if j + nums[j] >= next_i + nums[next_i]:
                    next_i = j
            i = next_i
            n_steps += 1
        return n_steps