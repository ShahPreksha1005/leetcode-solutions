# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to start the resultant linked list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2:
            # Sum the values of the two nodes plus the carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            # Update the carry for the next addition
            carry = total // 10
            # Create a new node with the digit value of total modulo 10
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in the linked lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there is a carry left, create a new node with the carry value
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the next node of the dummy node, which is the head of the resultant linked list
        return dummy.next

# Example Usage
# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: 7 -> 0 -> 8
