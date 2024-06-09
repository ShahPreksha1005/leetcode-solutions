import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshapes the DataFrame from wide to long format so that each row represents sales data for a product in a specific quarter.

    Parameters:
    report (pd.DataFrame): The input DataFrame with columns 'product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'.

    Returns:
    pd.DataFrame: The reshaped DataFrame.
    """
    # Use the melt function to reshape the DataFrame
    melted_df = pd.melt(report, id_vars=['product'], 
                        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
                        var_name='quarter', value_name='sales')
    
    return melted_df

# Example DataFrame
report = pd.DataFrame({
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
})

# Reshape the DataFrame and print the result
result = meltTable(report)
print(result)
