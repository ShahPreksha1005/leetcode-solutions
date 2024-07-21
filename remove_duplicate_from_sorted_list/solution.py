# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Edge case: empty list or single node
        if not head or not head.next:
            return head
        
        current = head
        
        while current and current.next:
            # If current node's value is the same as next node's value
            if current.val == current.next.val:
                # Skip the next node by adjusting pointers
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        return head
