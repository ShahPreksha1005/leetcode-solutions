import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Pivots the weather DataFrame so that each row represents temperatures for a specific month,
    and each city is a separate column.

    Parameters:
    weather (pd.DataFrame): The input DataFrame with columns 'city', 'month', and 'temperature'.

    Returns:
    pd.DataFrame: The pivoted DataFrame.
    """
    # Use pivot_table to pivot the DataFrame
    pivoted_df = weather.pivot(index='month', columns='city', values='temperature')
    
    # Reset the column names to remove the multi-level index
    pivoted_df.columns.name = None
    
    # Return the pivoted DataFrame without resetting the index
    return pivoted_df

# Example DataFrame
weather = pd.DataFrame({
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May', 
              'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
})

# Pivot the DataFrame and print the result
result = pivotTable(weather)
print(result)
