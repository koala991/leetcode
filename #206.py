# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        index = 0
        null_head = ListNode(None)
        null_head.next = head
        pre = null_head
        curr = head
        while curr is not None:
            index += 1
            if index < m or index > n:
                pre = curr
                curr = curr.next
            elif index == m:
                pre_block_tail = pre
                reversed_block_tail = curr
                pre = curr
                curr = curr.next
            elif index > m and index < n:
                _tmp = curr.next
                curr.next = pre
                pre = curr
                curr = _tmp
            elif index == n:
                pre_block_tail.next = curr
                reversed_block_tail.next = curr.next
                curr.next = pre
                pre = reversed_block_tail
                curr = reversed_block_tail.next
            else:
                pass
        return null_head.next