
## Concatenate Tables

**Problem Statement:**
You are given two DataFrames, `df1` and `df2`, containing student data with columns `student_id`, `name`, and `age`. Write a solution to concatenate these two DataFrames vertically into one DataFrame.

**Approach:**
We use the `pd.concat` function from the pandas library to concatenate the two DataFrames vertically. The `ignore_index=True` parameter ensures that the resulting DataFrame has a new continuous index.

**Detailed Steps:**
1. **Import pandas**: Import the pandas library to work with DataFrames.
2. **Define the function**: `concatenateTables(df1, df2)` takes two DataFrames as input and returns a concatenated DataFrame.
3. **Concatenate DataFrames**: Use `pd.concat([df1, df2], ignore_index=True)` to concatenate the DataFrames vertically, ignoring the original indices.
4. **Return the result**: Return the concatenated DataFrame.

**Example Data:**
```python
df1 = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
})

df2 = pd.DataFrame({
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
})
```

**Example Usage:**
```python
result = concatenateTables(df1, df2)
print(result)
```

**Expected Output:**
```
   student_id     name  age
0           1    Mason    8
1           2      Ava    6
2           3   Taylor   15
3           4  Georgia   17
4           5      Leo    7
5           6     Alex    7
```

**Explanation:**
The two DataFrames are concatenated vertically, resulting in a new DataFrame where all rows from `df1` are followed by all rows from `df2`. The original indices are ignored and a new continuous index is created.
