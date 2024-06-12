class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If numRows is 1, return the original string
        if numRows == 1:
            return s
        
        # Initialize a list of strings to store characters in each row
        rows = [''] * min(numRows, len(s))
        # Initialize variables for current row and direction of movement
        cur_row, going_down = 0, False
        
        # Iterate through each character in the string
        for char in s:
            # Append the character to the current row
            rows[cur_row] += char
            # Change the direction of movement when reaching the top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            # Update the current row based on the direction of movement
            cur_row += 1 if going_down else -1
        
        # Concatenate all rows to form the zigzag pattern
        return ''.join(rows)
