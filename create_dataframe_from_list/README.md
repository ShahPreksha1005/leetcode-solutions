
### Create a DataFrame from List

**Problem Statement:**
Given a 2D list called `student_data` containing IDs and ages of students, create a DataFrame with columns `student_id` and `age`.

**Approach:**
We use the pandas library in Python to create a DataFrame from the provided 2D list.

**Implementation:**
- Use the pandas library to create a DataFrame from the provided 2D list.
- Specify the column names while creating the DataFrame.

**Example Usage:**
```python
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
df = create_dataframe(student_data)
print(df)
```