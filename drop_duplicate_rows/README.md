
### Drop Duplicate Rows

**Problem Statement:**
There are some duplicate rows in the DataFrame based on the email column. Write a solution to remove these duplicate rows and keep only the first occurrence.

**Approach:**
We create a DataFrame from the provided data and drop duplicate rows based on the email column, keeping only the first occurrence.

**Implementation:**
- Create a DataFrame from the provided data.
- Drop duplicate rows based on the email column, keeping only the first occurrence.

**Example Usage:**
```python
customers = [
    (1, 'Ella', 'emily@example.com'),
    (2, 'David', 'michael@example.com'),
    (3, 'Zachary', 'sarah@example.com'),
    (4, 'Alice', 'john@example.com'),
    (5, 'Finn', 'john@example.com'),
    (6, 'Violet', 'alice@example.com')
]
result = drop_duplicate_rows(customers)
print(result)
```