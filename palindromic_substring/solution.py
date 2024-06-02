### Palindromic Substring

class Solution:

    def isPalindrome(self, s, left, right):
        """
        Check if the substring s[left:right+1] is a palindrome.
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def countSubstrings(self, s: str) -> int:
        """
        Count the number of palindromic substrings in the given string s.
        """
        count = 0
        n = len(s)
        
        # Iterate over all possible substrings and check if each one is a palindrome
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    count += 1
        return count