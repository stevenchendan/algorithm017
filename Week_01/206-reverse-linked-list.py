# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # iterative
#         if head is None:
#             return None
#         previous = None
#         current = head
#         while (current is not None):
#             next = current.next
#             current.next = previous
#             previous = current
#             current = next
#         return previous
    
        # recursive
        if head is None or head.next is None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
        