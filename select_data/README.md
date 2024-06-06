### Select Data

**Problem Statement:**
Given a DataFrame `students` with columns `student_id`, `name`, and `age`, select the name and age of the student with `student_id = 101`.

**Approach:**
We create a DataFrame from the provided data and use DataFrame indexing to select the name and age of the student with `student_id = 101`.

**Implementation:**
- Create a DataFrame from the provided data.
- Select the name and age where `student_id` equals 101 using DataFrame indexing.

**Example Usage:**
```python
students = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}
selected_info = select_student_info(students.values())
print(selected_info)
```
