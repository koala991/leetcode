# codind=utf-8

"""
构建长度为K的最小堆, add操作将新元素与根比较
注意点: 
1. 堆的操作还需要进一步熟悉, 边界的处理还不熟练, 本次问题主要都出在这.
2. 细节问题很多, debug才找出来, 熟练度不够 + 集中度不够 
"""
class MinHeap(list):
    def __init__(self, max_size):
        super(MinHeap, self).__init__()
        self.max_size = max_size
            
    def push(self, val):
        if self.size >= self.max_size:
            raise Exception("Out of heap size")
        else:
            self.append(val)
            self.shift_up()
        return

    def pop_root(self):
        self[0], self[self.size - 1] = self[self.size - 1], self[0]
        val = self.pop(self.size - 1)
        if self.size > 1:
            self.shift_down()
        return val

    def shift_up(self):
        i = self.size - 1
        while i > 0:
            if self[i] <= self[(i - 1) // 2]:
                self[i], self[(i - 1) // 2] = self[(i - 1) // 2], self[i]
                i = (i -1) // 2
            else:
                break
        return

    def shift_down(self):
        i = 0
        l_child, r_child = 2 * i + 1, 2 * i + 2
        while 2 * i + 1 < self.size:
            l_child, r_child = 2 * i + 1, 2 * i + 2            
            if r_child >= self.size or self[l_child] <= self[r_child]:
                min_child = l_child
            else:
                min_child = r_child

            if self[i] > self[min_child]:
                self[i], self[min_child] = self[min_child], self[i]
                i = min_child
            else:
                break


        return
    
    @property
    def size(self):
        return self.__len__()
    
    @property
    def root(self):
        return self[0]


class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    def __init__(self, k, nums):
        self.heap = MinHeap(k)
        for _num in nums:
            self.update_topk_heap(_num)

    def update_topk_heap(self, val):
        if self.heap.size < self.heap.max_size:
            self.heap.push(val)
        elif val > self.heap.root:
            self.heap.pop_root()
            self.heap.push(val)
        else:
            pass
        return

    # def add(self, val: int) -> int:
    def add(self, val):
        output = None
        self.update_topk_heap(val)
        if self.heap.size == self.heap.max_size:
            output = self.heap.root
        return output        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


if __name__ == "__main__":
    # k = 3
    # init = [4, 5, 8, 2]
    # klargest = KthLargest(1, init)
    # for val in [3, 5, 10, 9, 4]:
    #     print(klargest.add(val))

    # k = 1
    # init = []
    # klargest = KthLargest(k, init)
    # for val in [-3, -2, -4, 0, 4]:
    #     print(klargest.add(val))

    k = 7
    init = [-10,1,3,1,4,10,3,9,4,5,1]
    klargest = KthLargest(k, init)
    for val in [[3],[2],[3],[1],[2],[4],[5],[5],[6],[7],[7],[8],[2],[3],[1],[1],[1],[10],[11],[5],[6],[2],[4],[7],[8],[5],[6]]:
        print(klargest.add(*val))

