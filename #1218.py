from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        status = {}
        for i in arr:
            if i - difference in status:
                before_len = status.pop(i - difference)
            else:
                before_len = 0
            status[i] = max(before_len + 1, status.get(i, 0))
        return max(status.values())