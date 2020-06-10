class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] != "]":
                stack.append(s[i])
            else:
                tmp_strs = []
                while True:
                    if stack[-1] == "[":
                        int_str = []
                        _ = stack.pop(-1)
                        while len(stack) > 0 and stack[-1].isnumeric():
                            int_str.append(stack.pop(-1)) 
                        reverse(int_str)
                        n_repeats = int(''.join(int_str))
                        break
                    elif len(stack) == 0:
                        raise
                    else:
                        tmp_strs.append(stack.pop(-1))
                reverse(tmp_strs)
                stack.append(''.join(tmp_strs * n_repeats))
            i += 1
        return ''.join(stack)

def reverse(arr: list) -> list:
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return
