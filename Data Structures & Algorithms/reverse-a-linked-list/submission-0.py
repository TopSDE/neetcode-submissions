# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head):
        if not head.next:
            return head

        prev = head
        next_head = head.next
        curr_head = self.reverseLL(head.next)
        prev.next = None
        next_head.next = prev

        return curr_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        return self.reverseLL(head)