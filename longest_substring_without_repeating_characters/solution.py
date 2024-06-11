class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last positions of each character
        char_index = {}
        # Initialize the start of the current window and max length
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            # If the character is already in the dictionary and is in the current window
            if char in char_index and char_index[char] >= start:
                # Move the start to the next position of the last occurrence
                start = char_index[char] + 1
            # Update the last position of the character
            char_index[char] = i
            # Calculate the length of the current window
            max_length = max(max_length, i - start + 1)

        return max_length
