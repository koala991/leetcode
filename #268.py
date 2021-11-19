from functools import reduce
from operator import xor
from typing import List
from itertools import chain


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, chain(range(len(nums) + 1), nums))


if __name__ == "__main__":
    nums = [3,0,1]
    ans = Solution().missingNumber(nums)
    print(ans)
