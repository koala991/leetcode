# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseList_2(head)

    def reverseList_1(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pre, now = None, head
        while True:
            tmp = now.next
            now.next = pre
            pre = now
            now = tmp
            if now is None: break
        return pre

    def reverseList_2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        reversed_next = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None
        return reversed_next