# codind=utf-8

class Solution:
    def reverse(self, x: int) -> int:
        is_negtive = 1 if x < 0 else 0 
        x = -x if x < 0 else x
        y = int(str(x)[::-1])        
        if y - is_negtive > 2147483647:
            y = 0
        else:
            if is_negtive:
                y = -y
        return y

