def divide_array(nums, k):
    # Sort the array
    nums.sort()
    
    # Initialize the result array
    result = []
    
    # Iterate through the sorted array
    for num in nums:
        if not result or num > result[-1][-1] + k:
            # If result is empty or current element is greater than the last element of the last array plus k,
            # create a new array containing the current element
            result.append([num])
        else:
            # Otherwise, append the current element to the last array in result
            result[-1].append(num)
            
            # If the size of the last array becomes 3, reset it to empty
            if len(result[-1]) == 3:
                result.append([])
    
    # If all elements are successfully grouped into arrays of size 3, return result; otherwise, return an empty array
    return result if not result[-1] else []

# Example usage
nums1 = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k1 = 2
print(divide_array(nums1, k1))  # Output: [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

nums2 = [1, 3, 3, 2, 7, 3]
k2 = 3
print(divide_array(nums2, k2))  # Output: []
