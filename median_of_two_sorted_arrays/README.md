# LeetCode Problem: Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

### Example 1:
- **Input:** `nums1 = [1,3]`, `nums2 = [2]`
- **Output:** `2.00000`
- **Explanation:** Merged array = `[1,2,3]` and median is 2.

### Example 2:
- **Input:** `nums1 = [1,2]`, `nums2 = [3,4]`
- **Output:** `2.50000`
- **Explanation:** Merged array = `[1,2,3,4]` and median is `(2 + 3) / 2 = 2.5`.

### Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Solution

### Approach
The problem can be solved using the concept of binary search. Here are the steps taken:

1. **Ensure nums1 is the smaller array**: If nums1 is larger than nums2, swap the arrays to ensure nums1 is smaller.

2. **Define binary search boundaries**: The boundaries for the binary search will be between 0 and the length of nums1.

3. **Perform binary search**: Within each iteration of the binary search, partition nums1 and nums2 at the middle. Then, calculate the boundary elements of the partitions and compare them. Adjust the boundaries accordingly based on the comparison results.

4. **Calculate the median**: Once a valid partition is found, calculate the median based on the total length of the merged array and return it.

### Code Explanation
The provided Python code implements the binary search approach to find the median of two sorted arrays. Detailed comments are provided within the code to explain each step.

## Complexity Analysis
- **Time Complexity**: O(log(min(m, n))), where m and n are the lengths of the two input arrays.
- **Space Complexity**: O(1), as only a constant amount of extra space is used.

## Usage

You can use the `Solution` class to find the median of two sorted arrays. Here is how you can do it in Python:

```python
nums1 = [1, 3]
nums2 = [2]

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 2.00000
