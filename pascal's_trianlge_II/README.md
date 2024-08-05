
#### Pascal's Triangle II

Given an integer `rowIndex`, return the `rowIndex`th (0-indexed) row of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it. The triangle starts with a single 1 at the top.

##### Example:

1. Input: `rowIndex = 3`
   Output: `[1, 3, 3, 1]`

   Explanation: The 4th row (0-indexed) of Pascal's triangle is `[1, 3, 3, 1]`.

2. Input: `rowIndex = 0`
   Output: `[1]`

   Explanation: The 1st row of Pascal's triangle is `[1]`.

3. Input: `rowIndex = 1`
   Output: `[1, 1]`

   Explanation: The 2nd row of Pascal's triangle is `[1, 1]`.

##### Constraints:

- 0 <= rowIndex <= 33

##### Follow Up:

Optimize the algorithm to use only O(rowIndex) extra space.

---