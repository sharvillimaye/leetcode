# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        current = head
        visited = set()
        while current != None:
            if current not in visited:
                visited.add(current)
            else:
                return True
            current = current.next
        
        return False
        