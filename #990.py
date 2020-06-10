"""
构建使相等变量归属同一头结点的图/树，首先遍历“==”条件获得全结构树, "!="条件先压入栈，完成一次遍历后再取出.
用哈希表(字典)标记根节点实现
"""
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        inequal_stack = []
        root_map = {}
        i_assign = 1
        for equ in equations:
            var1, cond, var2 = self.split(equ)
            if cond == "!=":
                inequal_stack.append((var1, cond, var2))
            elif cond == "==":
                if var1 not in root_map and var2 not in root_map:
                    root_map[var1] = i_assign
                    root_map[var2] = i_assign
                    i_assign += 1
                elif var1 in root_map and var2 in root_map:
                    for key, val in root_map.items():
                        if val == root_map[var2] and key != var2:
                            root_map[key] = root_map[var1]
                    root_map[var2] = root_map[var1]
                elif var1 in root_map:
                    root_map[var2] = root_map[var1]
                else:
                    root_map[var1] = root_map[var2]
            else:
                raise

        output = True
        for  var1, _, var2 in inequal_stack:
            if (var1 == var2
                or (var1 in root_map and var2 in root_map and root_map[var1] == root_map[var2])
                ):
                output = False
                break
        return output

    def split(self, equation):
        s1, s2, s3 = 0, 0, 0
        i = 0
        while s3 == 0:
            if s2 == 0  and equation[i] in ("!", "="):
                s2 = i
            if s2 > 0  and equation[i] not in ("!", "="):
                s3 = i
            i += 1
        return equation[s1: s2], equation[s2: s3], equation[s3:]