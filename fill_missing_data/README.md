
### Fill Missing Data

**Problem Statement:**
Fill missing values as 0 in the quantity column.

**Approach:**
We create a DataFrame from the provided data and fill missing values as 0 in the quantity column.

**Implementation:**
- Create a DataFrame from the provided data.
- Fill missing values as 0 in the quantity column using the `fillna` method.

**Example Usage:**
```python
products = [
    ('Wristwatch', None, 135),
    ('WirelessEarbuds', None, 821),
    ('GolfClubs', 779, 9319),
    ('Printer', 849, 3051)
]
result = fill_missing_data(products)
print(result)
```
