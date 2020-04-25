# codind=utf-8

class Solution:
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        max_length = 0
        while right < len(s):
            if s[right] in s[left: right]:
                if right - 1 - left + 1 > max_length:
                    max_length = right - 1 - left + 1
                index = s[left: right].index(s[right]) + left
                left = index + 1
                right += 1
            else:
                right += 1
            
        right -= 1 # 循环出来比实际表示的含义大1, 捕捉最后一次没有重复结束循环的情况
        if right - left + 1 > max_length:
            max_length = right - left + 1
        return max_length

if __name__ == "__main__":
    s = "dvdf"
    print(Solution().lengthOfLongestSubstring(s))


# codind=utf-8

class Solution:
    def addTwoNumbers(self, l1, l2):
        output = []
        forward = 0
        for i in range(max(len(l1), len(l2))):
            # _x1 = l1.pop(0) if len(l1) > 0 else 0
            _x1 = l1.pop(0) if l1 else 0
            _x2 = l2.pop(0) if l2 else 0
            _x3 = _x1 + _x2 + forward
            forward = _x3 // 10
            output.append(_x3 % 10)
        if forward > 0:
            output.append(forward)
        return output

