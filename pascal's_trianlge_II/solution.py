class Solution:
    def getRow(self, rowIndex: int):
        # Initialize the first row as [1]
        row = [1]

        # Iterate to build the row for the given rowIndex
        for i in range(1, rowIndex + 1):
            # Calculate the new row using the previous row's values
            # Add a 0 to the beginning and end of the current row for calculation
            row = [x + y for x, y in zip([0] + row, row + [0])]

        return row
