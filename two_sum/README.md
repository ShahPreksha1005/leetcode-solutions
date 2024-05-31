Two Sum

Problem Statement:

Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Examples:

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Solution:

The solution uses a dictionary to keep track of the indices of the numbers we have seen so far. For each number in the array, we check if its complement (target - current number) is in the dictionary. If it is, we return the indices of the current number and its complement. If not, we add the current number and its index to the dictionary.

Code:

(class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the value and its index
        num_dict = {}

        # Enumerate over the list to get both index and value
        for i, num in enumerate(nums):
            # Calculate the complement that when added to the current number equals the target
            complement = target - num
            
            # If the complement is found in the dictionary, return the indices
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

        # If no solution is found (though the problem guarantees one solution), return an empty list
        return []

Example usage:

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]

How to Run:

1. Ensure you have Python installed on your system.
2. Save the code in a file named 'solution.py'.
3. Open a terminal and navigate to the directory containing 'solution.py'.
4. Run the script using the command:
    python solution.py

Explanation:

- Dictionary Storage: We use a dictionary to store each number and its index as we iterate through the list.
- Complement Check: For each number, we compute its complement (i.e., 'target - num'). If the complement exists in the dictionary, we have found our solution and return the indices.
- Adding to Dictionary: If the complement is not found, we add the current number and its index to the dictionary and continue.

Time Complexity:

The time complexity of this solution is O(n), where n is the number of elements in the array. This is because we traverse the list only once, and dictionary operations (insertion and lookup) are O(1) on average.

Space Complexity:

The space complexity is also O(n), due to the space required to store the dictionary.
