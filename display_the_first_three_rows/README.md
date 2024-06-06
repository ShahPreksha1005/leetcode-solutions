### Display the First Three Rows

**Problem Statement:**
Given a DataFrame `employees`, display the first three rows of the DataFrame.

**Approach:**
We create a DataFrame from the provided data and use the `head()` method in pandas to display the first three rows of the DataFrame.

**Implementation:**
- Create a DataFrame from the provided data.
- Use the `head()` method to display the first three rows of the DataFrame.

**Example Usage:**
```python
employees = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}
first_three_rows = display_first_three_rows(employees.values())
print(first_three_rows)
```