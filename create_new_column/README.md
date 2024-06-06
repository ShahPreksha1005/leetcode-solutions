
### Create a New Column

**Problem Statement:**
A company plans to provide its employees with a bonus. Write a solution to create a new column named bonus that contains doubled values of the salary column.

**Approach:**
We create a DataFrame from the provided data and add a new column named 'bonus' by doubling the values in the 'salary' column.

**Implementation:**
- Create a DataFrame from the provided data.
- Add a new column named 'bonus' containing doubled values of the 'salary' column.

**Example Usage:**
```python
employees = [
    ('Piper', 4548),
    ('Grace', 28150),
    ('Georgia', 1103),
    ('Willow', 6593),
    ('Finn', 74576),
    ('Thomas', 24433)
]
result = add_bonus_column(employees)
print(result)
```
