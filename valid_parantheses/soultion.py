class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the topmost element from the stack if it's not empty; otherwise, assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the top element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty at the end, all brackets were matched correctly
        return not stack
