# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head

        void_head = ListNode(None)
        void_head.next = head
        i = 0
        pre, curr = void_head, head
        pre_tail, curr_tail = None, None
        while curr is not None:
            if i % k == 0:
                pre_tail, curr_tail = pre, curr
            elif i % k == k - 1:
                curr_head, next_head = curr, curr.next
            pre = curr
            curr = curr.next

            if i % k == k - 1:
                tmp_pre, tmp_curr = curr_tail, curr_tail.next
                for _ in range(k - 1):
                    _tmp = tmp_curr.next
                    tmp_curr.next = tmp_pre
                    tmp_pre = tmp_curr
                    tmp_curr = _tmp
                pre_tail.next = curr_head
                curr_tail.next = next_head
                pre = curr_tail

            i += 1
            
        return void_head.next