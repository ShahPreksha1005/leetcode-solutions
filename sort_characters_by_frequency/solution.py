###  Characters by Frequency

from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of characters in the string
        counter = Counter(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        result = ''
        
        # Pop characters from the heap and append them to the result string
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * -freq
        return result
