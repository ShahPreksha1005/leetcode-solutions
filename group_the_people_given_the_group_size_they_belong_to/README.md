# Group the People Given the Group Size They Belong To

## Problem Statement

There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array `groupSizes`, where `groupSizes[i]` is the size of the group that person `i` is in. For example, if `groupSizes[1] = 3`, then person 1 must be in a group of size 3.

Return a list of groups such that each person `i` is in a group of size `groupSizes[i]`.

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

## Examples

### Example 1
Input: `groupSizes = [3,3,3,3,3,1,3]`  
Output: `[[5], [0, 1, 2], [3, 4, 6]]`

### Example 2
Input: `groupSizes = [2,1,3,3,3,2]`  
Output: `[[1], [0, 5], [2, 3, 4]]`

## Constraints

- `groupSizes.length == n`
- `1 <= n <= 500`
- `1 <= groupSizes[i] <= n`

## Solution

We solve this problem by grouping people based on their required group sizes. We use a dictionary to collect indices of people according to their group size and then form groups by iterating through these collected indices.

### Approach
1. **Group People by Size**: Use a dictionary to collect indices of people according to their required group size.
2. **Form Groups**: Iterate through the dictionary and create groups of the required sizes using the collected indices.

### Code

```python
def groupThePeople(groupSizes):
    from collections import defaultdict
    
    # Dictionary to collect people by group size
    size_to_people = defaultdict(list)
    
    # Collect indices of people according to their group size
    for person_id, size in enumerate(groupSizes):
        size_to_people[size].append(person_id)
    
    # List to store the final groups
    result = []
    
    # Form groups according to the collected sizes
    for size, people in size_to_people.items():
        # Iterate over the people list in chunks of 'size'
        for i in range(0, len(people), size):
            # Form a group of 'size' people
            group = people[i:i+size]
            result.append(group)
    
    return result

# Example usage
print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))  # Output: [[5], [0, 1, 2], [3, 4, 6]]
print(groupThePeople([2, 1, 3, 3, 3, 2]))    # Output: [[1], [0, 5], [2, 3, 4]]
