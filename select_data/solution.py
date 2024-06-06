import pandas as pd

def select_student_info(students):
    # Create DataFrame from the provided data
    df = pd.DataFrame(students)
    
    # Select name and age where student_id equals 101
    selected_info = df.loc[df['student_id'] == 101, ['name', 'age']]
    
    return selected_info

# Example usage
students = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

selected_info = select_student_info(students.values())
print(selected_info)
