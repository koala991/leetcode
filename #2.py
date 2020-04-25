# codind=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        head_node = ListNode(0)
        last_node = head_node
        forward = 0
        while l1 or l2:
            _x1 = l1.val if l1 else 0
            _x2 = l2.val if l2 else 0
            _x3 = _x1 + _x2 + forward 
            forward = _x3 // 10
            last_node.next = ListNode(_x3 % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            last_node = last_node.next
        if forward > 0:
            last_node.next = ListNode(forward)
        return head_node.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(l1, l2))



