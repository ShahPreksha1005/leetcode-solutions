# LeetCode Problem: Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example 1:
- **Input:** `l1 = [2,4,3]`, `l2 = [5,6,4]`
- **Output:** `[7,0,8]`
- **Explanation:** 342 + 465 = 807.

### Example 2:
- **Input:** `l1 = [0]`, `l2 = [0]`
- **Output:** `[0]`

### Example 3:
- **Input:** `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`
- **Output:** `[8,9,9,9,0,0,0,1]`

### Constraints:
- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Solution

### Approach
The solution uses a straightforward approach to simulate the addition of two numbers represented as linked lists. Here are the steps taken:

1. **Initialize Dummy Node**: Use a dummy node to help build the result linked list. This simplifies the code as we always have a node to append new results to.
2. **Initialize Carry**: Keep track of the carry from each addition of digits.
3. **Traverse Both Lists**: Traverse both linked lists until both are fully processed.
4. **Add Corresponding Digits**: Add the values of the corresponding digits along with any carry from the previous addition.
5. **Update Carry**: Update the carry based on the result of the addition.
6. **Create New Node**: Create a new node with the result of the addition modulo 10.
7. **Handle Remaining Carry**: If there is any carry left after the loop, create a new node for the carry.
8. **Return Result**: Return the next node of the dummy node, which points to the head of the resultant linked list.

### Code Explanation (Python)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy.next
