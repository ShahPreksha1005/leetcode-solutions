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
