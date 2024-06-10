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

# Example Usage
sol = Solution()
print(sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Output: True
print(sol.isNStraightHand([1,2,3,4,5], 4))          # Output: False
