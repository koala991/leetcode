# codind=utf-8
"""Definition for singly-linked list."""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        print("(", end="")
        tmp_node = self
        print(tmp_node.val, end="")
        while tmp_node.next:
            print(" -> ", end="")
            print(tmp_node.next.val, end="")
            tmp_node = tmp_node.next
        print(")")


class Solution:
    def addTwoNumbers(self, l1, l2):
        if not (l1 and l2):
            return l1 if l1 else l2
        tmp_l1, tmp_l2 = l1, l2
        l3 = ListNode(0)
        tmp_l3 = l3
        forward = 0
        while tmp_l1 or tmp_l2 or forward:
            if tmp_l1 and tmp_l2:
                tmp_div, tmp_mod = divmod(tmp_l1.val + tmp_l2.val, 10)
                tmp_l3.next = ListNode((tmp_mod + forward) % 10)
                forward = tmp_div + (tmp_mod + forward) // 10
                tmp_l1, tmp_l2, tmp_l3 = tmp_l1.next, tmp_l2.next, tmp_l3.next
            else:
                tmp_l3.next = Solution().addTwoNumbers(ListNode(forward), tmp_l1 if tmp_l1 else tmp_l2)
                break
        return l3.next


if __name__ == "__main__":
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    l1 = ListNode(5)
    l1.next = ListNode(5)

    l2 = ListNode(5)

    Solution().addTwoNumbers(l1, l2).show()



