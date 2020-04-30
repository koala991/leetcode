# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        right_head = ListNode(None)
        right_tail = right_head
        left_head = ListNode(None)
        left_tail = left_head
        curr = head
        while curr is not None:
            if curr.val < x:
                left_tail.next = curr
                left_tail = left_tail.next
            else:
                right_tail.next = curr
                right_tail = right_tail.next
            tmp = curr.next
            curr.next = None
            curr = tmp
        left_tail.next = right_head.next
        return left_head.next

if __name__ == "__main__":
    head = ListNode(None)
    tail = head
    for _x in [1,4,3,2,5,2]:
        tail.next = ListNode(_x)
        tail = tail.next
    x = 3
    result = Solution().partition(head.next, 3)
    _n = result
    while _n is not None:
        print(_n.val)
        _n = _n.next
    

