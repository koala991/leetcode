# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            l1, l2 = l2, l1
        elif l2 is not None and l1.val > l2.val:
            l1, l2 = l2, l1
        curr1 = l1
        curr2 = l2
        while curr2 is not None:
            while curr1.next is not None and curr1.next.val <= curr2.val:
                curr1 = curr1.next
            curr1.next, curr1 = curr2, curr1.next
            if curr1 is None: break
            while curr2.next is not None and curr2.next.val <= curr1.val:
                curr2 = curr2.next
            curr2.next, curr2 = curr1, curr2.next
        return l1
