class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        diff = right - left
        bits = self.get_bits(left)
        i_bits, i_tmp, l_tmp = [], 0, left

        while len(bits) > 0:
            i_bit = bits.pop()
            bit_one = ((1 << i_bit) - 1)
            need = (left & bit_one ^ bit_one) + 1
            if need > diff:
                res |= (1 << i_bit)
            else:
                break
        return res

    def get_bits(self, x):
        bits, i_tmp = [], 0
        while x > 0:
            if x & 1:
                bits += [i_tmp]
            x >>= 1
            i_tmp += 1
        return bits

# 标答
# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         i = 0
#         while left != right:
#             left >>= 1
#             right >>= 1
#             i += 1            
#         return left << i