class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [] # [(1, 1), (3, 1), ...]

    def push(self, x: int) -> None:
        if len(self.data) == 0:
            self.data.append((x, x)) 
        else:
            self.data.append((x, min(x, self.data[-1][1])))
        return 

    def pop(self) -> None:
        if len(self.data) > 0:
            x, x_min = self.data.pop(-1)
            return x 

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

