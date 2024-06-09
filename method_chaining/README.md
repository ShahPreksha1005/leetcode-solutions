
# Method Chaining for Finding Heavy Animals

This Python function `findHeavyAnimals` demonstrates the use of method chaining in pandas to efficiently filter and sort a DataFrame to find animals that weigh more than 100 kilograms. 

### Usage

```python
import pandas as pd

# Define the function findHeavyAnimals
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

# Example DataFrame
animals = pd.DataFrame({
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
})

# Using the function and printing the result
result = findHeavyAnimals(animals)
print(result)
```

### Function Explanation

1. **Filtering**: The function filters the DataFrame to keep only the rows where the 'weight' is greater than 100.
2. **Sorting**: The resulting DataFrame is then sorted by 'weight' in descending order.
3. **Selection**: Finally, only the 'name' column is selected for the output.

### Expected Output

```
       name
0   Tatiana
3  Jonathan
5     Tommy
2      Alex
```
