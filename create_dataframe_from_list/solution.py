import pandas as pd

def create_dataframe(student_data):
    # Define column names
    columns = ['student_id', 'age']
    
    # Create DataFrame from the 2D list with specified columns
    df = pd.DataFrame(student_data, columns=columns)
    
    return df

# Example usage
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

df = create_dataframe(student_data)
print(df)
