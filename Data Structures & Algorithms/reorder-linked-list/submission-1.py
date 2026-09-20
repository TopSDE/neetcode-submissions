# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(self, head):
        prev = None
        temp = head

        while temp:
            next_ = temp.next
            temp.next = prev
            prev = temp
            temp = next_

        return prev
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        new_head = self.rev(slow.next)
        slow.next = None

        curr1 = head
        curr2 = new_head
        curr1_next = curr1.next
        curr2_next = curr2.next

        while curr1_next and curr2_next:
            curr1.next = curr2
            curr2.next = curr1_next
            curr1 = curr1_next
            curr2 = curr2_next

            curr1_next = curr1_next.next
            curr2_next = curr2_next.next

        curr1.next = curr2