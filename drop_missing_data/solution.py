import pandas as pd

def drop_missing_data(students):
    """
    Drop rows with missing values in the name column.

    Parameters:
    students (list of tuples): List containing tuples with student_id, name, and age.

    Returns:
    pandas.DataFrame: DataFrame with rows containing missing values removed.
    """
    # Create DataFrame from the provided data
    df = pd.DataFrame(students, columns=['student_id', 'name', 'age'])
    
    # Drop rows with missing values in the name column
    df.dropna(subset=['name'], inplace=True)
    
    return df

# Example usage
students = [
    (32, 'Piper', 5),
    (217, None, 19),
    (779, 'Georgia', 20),
    (849, 'Willow', 14)
]

result = drop_missing_data(students)
print(result)
