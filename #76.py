# """
# 差两个例子
# """
# class CountSet(dict):
#     def add(self, x):
#         if x in self:
#             self[x] += 1
#         else:
#             self[x] = 1
#         return

#     def sub(self, x):
#         if x not in self or self[x] == 0:
#             raise KeyError("%s not in set" % x)
#         else:
#             self[x] -= 1
#             if self[x] == 0:
#                 self.pop(x)
#         return

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         met, need = CountSet(), CountSet()
#         for c in t:
#             need.add(c)

#         output = ""

#         j = 0
#         while j < len(s):
            
#             while j < len(s):
#                 if s[j] in need:
#                     need.sub(s[j])
#                     met.add(s[j])
#                 if len(need) == 0:
#                     break
#                 j += 1
        
#             if len(need) > 0:
#                 break

#             i = j
#             while i >= 0:
#                 if s[i] in met:
#                     met.sub(s[i])
#                     need.add(s[i])
#                 if len(met) == 0:
#                     break
#                 i -= 1

#             if len(output) == 0 or j - i + 1 < len(output):
#                 output = s[i: j + 1] 
            
#         return output



class CountSet(dict):
    def add(self, x):
        if x in self:
            self[x] += 1
        else:
            self[x] = 1
        return

    def sub(self, x):
        if x not in self or self[x] == 0:
            raise KeyError("%s not in set" % x)
        else:
            self[x] -= 1
            if self[x] == 0:
                self.pop(x)
        return

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        met, need, addtional = CountSet(), CountSet(), CountSet()
        for c in t:
            need.add(c)

        output = ""

        i, j = 0, 0
        while j < len(s):

            while j < len(s):
                if s[j] in need:
                    need.sub(s[j])
                    met.add(s[j])
                elif s[j] in met:
                    addtional.add(s[j])
                if len(need) == 0:
                    break
                j += 1
        
            if len(need) > 0:
                break

            while i < j:
                if s[i] in met and s[i] in addtional:
                    addtional.sub(s[i])
                elif s[i] in met and s[i] not in addtional:
                    met.sub(s[i])
                    need.add(s[i])
                    break
                i += 1

            if len(output) == 0 or j - i + 1 < len(output):
                output = s[i: j + 1] 

            j += 1
            i += 1
        return output


if __name__ == "__main__":
    solution = Solution()
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "acbbaca"
    t = "aba"    
    print(solution.minWindow(s, t))