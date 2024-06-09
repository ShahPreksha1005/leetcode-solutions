import pandas as pd

def fill_missing_data(products):
    """
    Fill missing values as 0 in the quantity column.

    Parameters:
    products (list of tuples): List containing tuples with name, quantity, and price.

    Returns:
    pandas.DataFrame: DataFrame with missing values filled in the quantity column.
    """
    # Create DataFrame from the provided data
    df = pd.DataFrame(products, columns=['name', 'quantity', 'price'])
    
    # Fill missing values as 0 in the quantity column
    df['quantity'].fillna(0, inplace=True)
    
    return df

# Example usage
products = [
    ('Wristwatch', None, 135),
    ('WirelessEarbuds', None, 821),
    ('GolfClubs', 779, 9319),
    ('Printer', 849, 3051)
]

result = fill_missing_data(products)
print(result)
