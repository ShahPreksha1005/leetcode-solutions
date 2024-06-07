import pandas as pd

def rename_columns(students):
    """
    Rename the columns as specified:
    id to student_id
    first to first_name
    last to last_name
    age to age_in_years

    Parameters:
    students (list of tuples): List containing tuples with id, first, last, and age.

    Returns:
    pandas.DataFrame: DataFrame with columns renamed.
    """
    # Create DataFrame from the provided data
    df = pd.DataFrame(students, columns=['id', 'first', 'last', 'age'])
    
    # Rename the columns
    df.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'}, inplace=True)
    
    return df

# Example usage
students = [
    (1, 'Mason', 'King', 6),
    (2, 'Ava', 'Wright', 7),
    (3, 'Taylor', 'Hall', 16),
    (4, 'Georgia', 'Thompson', 18),
    (5, 'Thomas', 'Moore', 10)
]

result = rename_columns(students)
print(result)
