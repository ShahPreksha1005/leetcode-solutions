### Solution:

class Solution {
    public int characterReplacement(String s, int k) {
        // Initialize an array to store the count of each character
        int[] charCount = new int[26];
        // Initialize variables to store the result and the maximum frequency of a single character in the current window
        int result = 0;
        int maxCount = 0;

        // The left pointer for the sliding window
        int left = 0;

        // Iterate over the string with the right pointer
        for (int right = 0; right < s.length(); right++) {
            // Update the count for the current character
            charCount[s.charAt(right) - 'A']++;

            // Update the maxCount to be the maximum frequency of any single character in the current window
            maxCount = Math.max(maxCount, charCount[s.charAt(right) - 'A']);

            // Check if the current window is valid
            // The window is valid if the number of changes needed is less than or equal to k
            // (right - left + 1) is the size of the window
            // maxCount is the maximum frequency of a single character in the current window
            // If the difference (window size - maxCount) is greater than k, the window is invalid
            if (right - left + 1 - maxCount > k) {
                // Decrement the count of the character at the left pointer
                charCount[s.charAt(left) - 'A']--;
                // Move the left pointer to the right
                left++;
            }

            // Update the result with the maximum window size seen so far
            result = Math.max(result, right - left + 1);
        }

        return result;
    }
}
