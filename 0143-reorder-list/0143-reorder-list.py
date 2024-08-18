# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow_pointer = head
        fast_pointer = head.next

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        stack = []
        curr = slow_pointer.next
        while curr:
            stack.append(curr)
            curr = curr.next
        
        slow_pointer.next = None
        current = head
        while current and stack:
            main_next = current.next
            current.next = stack.pop()
            current.next.next = main_next
            current = main_next