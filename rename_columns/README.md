
### Rename Columns

**Problem Statement:**
Write a solution to rename the columns as follows:
- id to student_id
- first to first_name
- last to last_name
- age to age_in_years

**Approach:**
We create a DataFrame from the provided data and rename the columns accordingly.

**Implementation:**
- Create a DataFrame from the provided data.
- Rename the columns using the `rename` method.

**Example Usage:**
```python
students = [
    (1, 'Mason', 'King', 6),
    (2, 'Ava', 'Wright', 7),
    (3, 'Taylor', 'Hall', 16),
    (4, 'Georgia', 'Thompson', 18),
    (5, 'Thomas', 'Moore', 10)
]
result = rename_columns(students)
print(result)
```
