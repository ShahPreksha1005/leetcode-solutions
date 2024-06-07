
### Modify Columns

**Problem Statement:**
A company intends to give its employees a pay rise. Write a solution to modify the salary column by multiplying each salary by 2.

**Approach:**
We create a DataFrame from the provided data and modify the salary column by multiplying each salary by 2.

**Implementation:**
- Create a DataFrame from the provided data.
- Modify the salary column by multiplying each salary by 2.

**Example Usage:**
```python
employees = [
    ('Jack', 19666),
    ('Piper', 74754),
    ('Mia', 62509),
    ('Ulysses', 54866)
]
result = modify_columns(employees)
print(result)
```
