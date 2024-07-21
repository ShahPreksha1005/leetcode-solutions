### Remove Duplicates from Sorted List

#### Problem Description

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

#### Examples

**Example 1:**

Input: `head = [1,1,2]`  
Output: `[1,2]`

**Example 2:**

Input: `head = [1,1,2,3,3]`  
Output: `[1,2,3]`

#### Constraints

- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be sorted in ascending order.

#### Solution

To solve this problem, we iterate through the linked list and remove duplicates by adjusting pointers. We start from the head and compare each node with its next node. If they have the same value, we skip the next node by adjusting pointers. If they have different values, we move to the next node. This approach ensures that each unique element appears only once in the list.

#### Code Explanation

```python
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
