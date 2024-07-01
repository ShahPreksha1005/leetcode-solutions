# LeetCode Problem: Merge Two Sorted Lists

## Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list by splicing together the nodes of the first two lists. Return the head of the merged linked list.

### Example 1:
- **Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]`
- **Output:** `[1,1,2,3,4,4]`

### Example 2:
- **Input:** `list1 = []`, `list2 = []`
- **Output:** `[]`

### Example 3:
- **Input:** `list1 = []`, `list2 = [0]`
- **Output:** `[0]`

### Constraints:
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Solution

### Approach
To merge the two sorted linked lists:
1. **Initialize a Dummy Node**: Create a dummy node to serve as the start of the merged list.
2. **Traverse and Compare**: Use two pointers to traverse the two lists, and compare the values at each step to build the new list.
3. **Attach Remaining Nodes**: Once one of the lists is fully traversed, attach the remaining nodes of the other list.
4. **Return Result**: Return the merged list starting from the node next to the dummy node.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

### Edge Cases
- If one or both lists are empty, the function handles this by simply returning the non-empty list or an empty list.

## Complexity Analysis
- **Time Complexity**: O(n + m), where `n` and `m` are the lengths of `list1` and `list2`, respectively. We traverse both lists completely.
- **Space Complexity**: O(1), as we only use a few extra variables and do not use additional space proportional to the input size.

## Usage

You can use the `Solution` class to merge two sorted linked lists. Here is how you can do it in Python:

```python
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_linked_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
