
### Drop Missing Data

**Problem Statement:**
There are some rows having missing values in the name column. Write a solution to remove these rows with missing values.

**Approach:**
We create a DataFrame from the provided data and drop rows with missing values in the name column.

**Implementation:**
- Create a DataFrame from the provided data.
- Drop rows with missing values in the name column.

**Example Usage:**
```python
students = [
    (32, 'Piper', 5),
    (217, None, 19),
    (779, 'Georgia', 20),
    (849, 'Willow', 14)
]
result = drop_missing_data(students)
print(result)
```
