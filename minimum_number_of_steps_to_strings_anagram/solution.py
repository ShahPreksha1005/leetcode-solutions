from collections import Counter

def minSteps(s, t):
    # Count the frequency of each character in both strings
    s_count = Counter(s)
    t_count = Counter(t)
    
    # Initialize the number of steps needed to 0
    steps = 0
    
    # Iterate over the character counts in s
    for char in s_count:
        # If the character is more frequent in s than in t,
        # calculate the difference and add it to steps
        if s_count[char] > t_count[char]:
            steps += s_count[char] - t_count[char]
    
    return steps

# Example usage
print(minSteps("bab", "aba"))         # Output: 1
print(minSteps("leetcode", "practice")) # Output: 5
print(minSteps("anagram", "mangaar"))   # Output: 0
