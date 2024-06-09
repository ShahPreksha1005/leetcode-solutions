
## Reshape Data: Pivot

**Problem Statement:**
You are given a DataFrame `weather` containing data about city temperatures for different months. Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

**Approach:**
We use the `pivot` function from the pandas library to reshape the data. The `pivot` function is used to create a new table from the existing DataFrame where the rows represent months and the columns represent cities.

**Detailed Steps:**
1. **Import pandas**: Import the pandas library to work with DataFrames.
2. **Define the function**: `pivotTable(weather)` takes a DataFrame as input and returns a pivoted DataFrame.
3. **Pivot the DataFrame**: Use `weather.pivot(index='month', columns='city', values='temperature')` to pivot the DataFrame.
4. **Reset the column names**: Ensure that the multi-level index for columns is removed by setting `pivoted_df.columns.name = None`.
5. **Return the result**: Return the pivoted DataFrame.

**Example Data:**
```python
weather = pd.DataFrame({
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May', 
              'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
})
```

**Example Usage:**
```python
result = pivotTable(weather)
print(result)
```

**Expected Output:**
```
           ElPaso  Jacksonville
month                          
April           2             5
February        6            23
January        20            13
March          26            38
May            43            34
```

**Explanation:**
The DataFrame is pivoted so that each city becomes a column and each month becomes a row. The temperatures for each city and month are filled into the corresponding cells.
