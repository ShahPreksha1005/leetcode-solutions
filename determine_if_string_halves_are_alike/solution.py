def halvesAreAlike(s: str) -> bool:
    # Define a set of vowels for quick lookup
    vowels = set('aeiouAEIOU')
    
    # Determine the length of each half
    n = len(s) // 2
    
    # Split the string into two halves
    a, b = s[:n], s[n:]
    
    # Function to count vowels in a given string
    def count_vowels(substring):
        return sum(1 for char in substring if char in vowels)
    
    # Count vowels in both halves
    count_a = count_vowels(a)
    count_b = count_vowels(b)
    
    # Return true if both halves have the same number of vowels
    return count_a == count_b

# Example usage
print(halvesAreAlike("book"))       # Output: true
print(halvesAreAlike("textbook"))   # Output: false
