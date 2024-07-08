class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the string s.

        Args:
        s (str): A string consisting of words and spaces.

        Returns:
        int: The length of the last word.
        """
        length = 0
        # Start from the end of the string and move backwards
        for i in range(len(s) - 1, -1, -1):
            # If we encounter a space after counting some characters, break
            if s[i] == ' ' and length > 0:
                break
            # If the character is not a space, increment the length counter
            elif s[i] != ' ':
                length += 1
        
        return length
