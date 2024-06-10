# LeetCode Problem: Hand of Straights

## Problem Statement
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the ith card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

### Example 1:
- **Input:** `hand = [1,2,3,6,2,3,4,7,8]`, `groupSize = 3`
- **Output:** `true`
- **Explanation:** Alice's hand can be rearranged as `[1,2,3], [2,3,4], [6,7,8]`.

### Example 2:
- **Input:** `hand = [1,2,3,4,5]`, `groupSize = 4`
- **Output:** `false`
- **Explanation:** Alice's hand cannot be rearranged into groups of 4.

### Constraints:
- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

## Solution

### Approach
The solution uses a greedy algorithm combined with a min-heap to achieve optimal time complexity. Here are the steps taken:

1. **Initial Check**: If the total number of cards is not divisible by `groupSize`, it's impossible to form the required groups, so return `False`.
2. **Count Frequencies**: Use a `Counter` from the `collections` module to count the frequency of each card.
3. **Min-Heap**: Use a min-heap to always process the smallest card value first.
4. **Form Groups**: Try to form groups starting from the smallest card. For each card, check if the consecutive cards required to form a group are available. If any card required to form a group is not available, return `False`.
5. **Adjust Counts**: Decrease the count of each card used. If the count of a card drops to zero, remove it from the heap to keep the heap clean.

### Code Explanation

```python
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # If the total number of cards is not divisible by groupSize, return False
        if len(hand) % groupSize != 0:
            return False

        # Count the frequency of each card
        count = Counter(hand)
        
        # Use a min-heap to process the cards in ascending order
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        
        # While there are cards left to process
        while min_heap:
            # Get the smallest card number
            first = min_heap[0]
            
            # Try to form a group starting with 'first'
            for i in range(first, first + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
                # If the count drops to zero, remove it from the heap
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
                    
        return True
