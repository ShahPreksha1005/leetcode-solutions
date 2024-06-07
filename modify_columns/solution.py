import pandas as pd

def modify_columns(employees):
    """
    Modify the salary column by multiplying each salary by 2.

    Parameters:
    employees (list of tuples): List containing tuples with employee name and salary.

    Returns:
    pandas.DataFrame: DataFrame with salary column modified.
    """
    # Create DataFrame from the provided data
    df = pd.DataFrame(employees, columns=['name', 'salary'])
    
    # Modify the salary column by multiplying each salary by 2
    df['salary'] *= 2
    
    return df

# Example usage
employees = [
    ('Jack', 19666),
    ('Piper', 74754),
    ('Mia', 62509),
    ('Ulysses', 54866)
]

result = modify_columns(employees)
print(result)
