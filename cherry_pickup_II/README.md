
### Cherry Pickup II

**Problem Statement:**
Given a matrix `grid` representing a field of cherries, determine the maximum number of cherries collected by two robots starting at the top-left and top-right corners and moving to the bottom row.

**Approach:**
We use dynamic programming to find the maximum number of cherries collected. We iterate through the grid row by row and calculate the maximum cherries collected at each step considering the positions of both robots.

**Implementation:**
- Use dynamic programming to calculate the maximum cherries collected.
- Iterate through the grid row by row and calculate the maximum cherries collected at each step considering the positions of both robots.

**Example Usage:**
```python
grid = [
    [3, 1, 1],
    [2, 5, 1],
    [1, 5, 5],
    [2, 1, 1]
]
print(cherryPickup(grid))  # Output: 24
```