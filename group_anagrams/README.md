# Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def getSignature(self, s: str) -> str:
        """
        Get the signature of a string, representing its character counts.
        
        Parameters:
        s (str): Input string.
        
        Returns:
        str: Signature representing character counts.
        """
        # Initialize an array to store the count of each character
        count = [0] * 26
        
        # Count occurrences of each character in the string
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Build the signature by concatenating characters and their counts
        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])
        
        return ''.join(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together.
        
        Parameters:
        strs (List[str]): List of input strings.
        
        Returns:
        List[List[str]]: List of grouped anagrams.
        """
        # Initialize an empty list to store the result
        result = []
        
        # Use defaultdict to store groups of anagrams
        groups = defaultdict(list)
        
        # Iterate over each string in the input list
        for s in strs:
            # Get the signature of the string
            signature = self.getSignature(s)
            
            # Append the string to its corresponding group based on the signature
            groups[signature].append(s)
        
        # Append values (groups of anagrams) to the result list
        result.extend(groups.values())
        
        return result
