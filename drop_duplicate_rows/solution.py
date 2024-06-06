import pandas as pd

def drop_duplicate_rows(customers):
    """
    Drop duplicate rows based on the email column and keep only the first occurrence.

    Parameters:
    customers (list of tuples): List containing tuples with customer_id, name, and email.

    Returns:
    pandas.DataFrame: DataFrame with duplicate rows removed.
    """
    # Create DataFrame from the provided data
    df = pd.DataFrame(customers, columns=['customer_id', 'name', 'email'])
    
    # Drop duplicate rows based on the email column and keep only the first occurrence
    df.drop_duplicates(subset=['email'], keep='first', inplace=True)
    
    return df

# Example usage
customers = [
    (1, 'Ella', 'emily@example.com'),
    (2, 'David', 'michael@example.com'),
    (3, 'Zachary', 'sarah@example.com'),
    (4, 'Alice', 'john@example.com'),
    (5, 'Finn', 'john@example.com'),
    (6, 'Violet', 'alice@example.com')
]

result = drop_duplicate_rows(customers)
print(result)
