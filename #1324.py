"""
没啥意思的一题
"""
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_l = s.split(" ")
        output = []
        i = 0
        while True:
            new_ = list(map(lambda x: x[i] if i < len(x) else ' ', s_l))
            new = "".join(new_).rstrip()
            if new == "": break
            output.append(new)
            i += 1
        return output
            