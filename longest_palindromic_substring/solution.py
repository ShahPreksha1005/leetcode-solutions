class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Function to expand around the center and find the longest palindrome
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the substring of the longest palindrome found
            return s[left + 1:right]

        # Initialize variables to store the start and end indices of the longest palindrome
        start, end = 0, 0

        # Iterate through each character in the string
        for i in range(len(s)):
            # Expand around the center for odd-length palindromes
            palindrome1 = expand_around_center(i, i)
            # Expand around the center for even-length palindromes
            palindrome2 = expand_around_center(i, i + 1)
            # Update the start and end indices if a longer palindrome is found
            if len(palindrome1) > len(palindrome2) and len(palindrome1) > end - start:
                start = i - len(palindrome1) // 2
                end = i + len(palindrome1) // 2
            elif len(palindrome2) > len(palindrome1) and len(palindrome2) > end - start:
                start = i - len(palindrome2) // 2 + 1
                end = i + len(palindrome2) // 2

        # Return the longest palindrome substring
        return s[start:end + 1]
