def minDeletions(s: str) -> int:
    from collections import Counter
    
    # Count the frequency of each character
    freq = Counter(s)
    
    # Get all frequencies and sort them in descending order
    frequencies = sorted(freq.values(), reverse=True)
    
    # Initialize a set to keep track of used frequencies
    used_frequencies = set()
    
    # Initialize the count of deletions
    deletions = 0
    
    for frequency in frequencies:
        # If the frequency is already used, we need to adjust it
        while frequency > 0 and frequency in used_frequencies:
            frequency -= 1
            deletions += 1
        # Add the adjusted frequency to the set of used frequencies
        used_frequencies.add(frequency)
    
    return deletions

# Example usage
print(minDeletions("aab"))         # Output: 0
print(minDeletions("aaabbbcc"))    # Output: 2
print(minDeletions("ceabaacb"))    # Output: 2
