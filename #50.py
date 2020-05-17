class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1.0
    #     elif n == 1:
    #         return x

    #     if n < 0:
    #         x = 1 / x
    #         n = -n

    #     output = self.myPow(x, n // 2)
    #     output *= output
    #     if n % 2 == 1: output *= x

    #     return output 
        
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1/x, -n

        output, x_pow = 1, x
        while n > 0:
            if n % 2: output *= x_pow
            x_pow *= x_pow
            n = n >> 1
        return output

