import pandas as pd

def display_first_three_rows(employees):
    # Create DataFrame from the provided data
    df = pd.DataFrame(employees)
    
    # Display the first three rows using head() method
    first_three_rows = df.head(3)
    
    return first_three_rows

# Example usage
employees = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

first_three_rows = display_first_three_rows(employees.values())
print(first_three_rows)
