import pandas as pd

def change_data_type(students):
    """
    Change the data type of the grade column from float to integer.

    Parameters:
    students (list of tuples): List containing tuples with student_id, name, age, and grade.

    Returns:
    pandas.DataFrame: DataFrame with grade column data type corrected.
    """
    # Create DataFrame from the provided data
    df = pd.DataFrame(students, columns=['student_id', 'name', 'age', 'grade'])
    
    # Change data type of the grade column from float to integer
    df['grade'] = df['grade'].astype(int)
    
    return df

# Example usage
students = [
    (1, 'Ava', 6, 73.0),
    (2, 'Kate', 15, 87.0)
]

result = change_data_type(students)
print(result)
