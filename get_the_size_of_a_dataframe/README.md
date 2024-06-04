
### Get the Size of a DataFrame

**Problem Statement:**
Given a DataFrame `players`, calculate and display the number of rows and columns of the DataFrame.

**Approach:**
We create a DataFrame from the provided data and use the `shape` attribute of the DataFrame to get the number of rows and columns.

**Implementation:**
- Create a DataFrame from the provided data.
- Use the `shape` attribute of the DataFrame to get the number of rows and columns.

**Example Usage:**
```python
players = {
    'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
    'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
    'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
    'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
}
size = dataframe_size(players.values())
print(size)
```