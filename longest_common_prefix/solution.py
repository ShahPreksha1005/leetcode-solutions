class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string in the list
        shortest = min(strs, key=len)
        
        # Iterate through the characters of the shortest string
        for i, char in enumerate(shortest):
            # Compare with the same position of other strings
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        
        return shortest
