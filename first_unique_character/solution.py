class Solution:
    def firstUniqChar(self, s):
        """
        Given a string s, find the first non-repeating character in it and return its index. 
        If it does not exist, return -1.

        Parameters:
        s (str): Input string.

        Returns:
        int: Index of the first non-repeating character, or -1 if none.

        Example:
        --------
        >>> solution = Solution()
        >>> solution.firstUniqChar("leetcode")
        0
        >>> solution.firstUniqChar("loveleetcode")
        2
        >>> solution.firstUniqChar("aabb")
        -1
        """
        # Dictionary to store character counts
        char_count = {}

        # Count occurrences of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Iterate over the string to find the first non-repeating character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no non-repeating character is found, return -1
        return -1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar("leetcode"))      # Output: 0
    print(solution.firstUniqChar("loveleetcode"))  # Output: 2
    print(solution.firstUniqChar("aabb"))          # Output: -1
