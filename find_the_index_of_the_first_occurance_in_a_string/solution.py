class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Args:
        haystack (str): The string to be searched.
        needle (str): The substring to search for.

        Returns:
        int: The index of the first occurrence of needle, or -1 if not found.
        """
        # Lengths of the haystack and the needle
        h_len = len(haystack)
        n_len = len(needle)
        
        # If needle is empty, return 0 (common convention)
        if n_len == 0:
            return 0
        
        # If haystack is shorter than needle, needle cannot be part of haystack
        if h_len < n_len:
            return -1
        
        # Iterate through the haystack using a sliding window of size equal to needle length
        for i in range(h_len - n_len + 1):
            # Check if the substring of haystack starting at i matches needle
            if haystack[i:i + n_len] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1
