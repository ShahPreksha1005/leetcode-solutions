### README

## Combination Sum IV

### Problem Description

Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

The test cases are generated so that the answer can fit in a 32-bit integer.

### Example 1

- **Input:** `nums = [1,2,3]`, `target = 4`
- **Output:** `7`
- **Explanation:**
  The possible combination ways are:
  - `(1, 1, 1, 1)`
  - `(1, 1, 2)`
  - `(1, 2, 1)`
  - `(1, 3)`
  - `(2, 1, 1)`
  - `(2, 2)`
  - `(3, 1)`
  
  Note that different sequences are counted as different combinations.

### Example 2

- **Input:** `nums = [9]`, `target = 3`
- **Output:** `0`

### Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 1000`
- All the elements of `nums` are unique.
- `1 <= target <= 1000`

### Follow-up

- **Question:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation do we need to add to the question to allow negative numbers?
- **Answer:** If negative numbers are allowed, it would introduce the possibility of infinite combinations because we could add and subtract the same number indefinitely. To handle this, we would need to impose a limit on the number of elements used or on the range of numbers.

### Solution Explanation

This solution uses dynamic programming to compute the number of ways to sum up to the target.

#### Detailed Explanation

1. **Imports and Class Definition:**
    - Import the `List` type from the `typing` module for type hinting.
    - Define a class named `Solution`.

2. **Method Definition:**
    - Define a method `combinationSum4` that takes a list of integers `nums` and an integer `target`, and returns an integer.

3. **Initialize DP Array:**
    - Create a list `dp` of length `target + 1`, initialized with zeros. This list will store the number of ways to achieve each sum from `0` to `target`.

4. **Base Case:**
    - There is one way to achieve a sum of `0`, which is by using no elements.

5. **Main DP Loop:**
    - Iterate over each integer `i` from `1` to `target`. For each `i`, we will determine the number of ways to form the sum `i`.

6. **Nested Loop Over `nums`:**
    - For each `i`, iterate over each number `num` in the list `nums`.

7. **Check Valid Subproblem:**
    - Check if `i - num` is non-negative. This ensures that we are only considering valid subproblems.

8. **Update DP Array:**
    - Update `dp[i]` by adding the number of ways to achieve the sum `i - num`. This works because if we can form the sum `i - num`, then by adding `num` to each combination that forms `i - num`, we get a way to form the sum `i`.

9. **Return Result:**
    - Return the number of ways to achieve the sum `target`, which is stored in `dp[target]`.

10. **Example Usage:**
    - The commented-out lines at the end of the script demonstrate how to create an instance of `Solution` and call the `combinationSum4` method with example inputs. These lines can be uncommented to run the examples.