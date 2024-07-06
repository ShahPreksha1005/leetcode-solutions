
# Search Insert Position

## Problem Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

## Examples

### Example 1

- **Input:** `nums = [1,3,5,6]`, `target = 5`
- **Output:** `2`

### Example 2

- **Input:** `nums = [1,3,5,6]`, `target = 2`
- **Output:** `1`

### Example 3

- **Input:** `nums = [1,3,5,6]`, `target = 7`
- **Output:** `4`

## Constraints

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` contains distinct values sorted in ascending order.
- `-104 <= target <= 104`

## Approach

To achieve O(log n) runtime complexity, we use binary search. The binary search technique helps to efficiently find the target or the insertion point in a sorted array.

## Solution

### Detailed Code with Comments

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Returns the index of the target in nums if found, otherwise the index where it would be inserted.

        Args:
        nums (List[int]): A sorted list of distinct integers.
        target (int): The target integer to search for.

        Returns:
        int: The index of the target if found, otherwise the index where it would be inserted.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Find the middle element
            
            if nums[mid] == target:
                return mid  # Target found at index mid
            elif nums[mid] < target:
                left = mid + 1  # Search the right half
            else:
                right = mid - 1  # Search the left half
        
        # If target is not found, left will be the insertion point
        return left
```

## Explanation

1. **Initialization:**
   - Set `left` to 0 and `right` to the last index of `nums`.

2. **Binary Search:**
   - Calculate the middle index `mid`.
   - If `nums[mid]` equals `target`, return `mid`.
   - If `nums[mid]` is less than `target`, move the `left` pointer to `mid + 1`.
   - If `nums[mid]` is greater than `target`, move the `right` pointer to `mid - 1`.

3. **Return Insertion Point:**
   - If the target is not found, the `left` pointer will indicate the insertion point.
