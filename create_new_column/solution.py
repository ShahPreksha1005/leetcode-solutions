import pandas as pd

def add_bonus_column(employees):
    """
    Add a bonus column to the DataFrame employees containing doubled values of the salary column.

    Parameters:
    employees (list of tuples): List containing tuples with employee name and salary.

    Returns:
    pandas.DataFrame: DataFrame with bonus column added.
    """
    # Create DataFrame from the provided data
    df = pd.DataFrame(employees, columns=['name', 'salary'])
    
    # Double the values in the salary column to create the bonus column
    df['bonus'] = df['salary'] * 2
    
    return df

# Example usage
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
