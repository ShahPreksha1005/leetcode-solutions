
### Change Data Type

**Problem Statement:**
The grade column is stored as floats, convert it to integers.

**Approach:**
We create a DataFrame from the provided data and change the data type of the grade column from float to integer.

**Implementation:**
- Create a DataFrame from the provided data.
- Change the data type of the grade column using the `astype` method.

**Example Usage:**
```python
students = [
    (1, 'Ava', 6, 73.0),
    (2, 'Kate', 15, 87.0)
]
result = change_data_type(students)
print(result)
```
