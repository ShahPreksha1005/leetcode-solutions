### Daily Temperatures

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures):
        # Initialize an empty deque to store indices of temperatures
        deq = deque()
        # Initialize an array to store the result
        res = [0] * len(temperatures)

        # Iterate through the temperatures array from right to left
        for i in range(len(temperatures) - 1, -1, -1):
            if not deq:
                # If the deque is empty, append the current index
                deq.appendleft(i)
                res[i] = 0
            else:
                # Pop elements from the left end of the deque until we find a warmer temperature
                while deq and temperatures[i] >= temperatures[deq[0]]:
                    deq.popleft()

                if not deq:
                    res[i] = 0
                else:
                    # Set the corresponding value in the result array
                    res[i] = deq[0] - i

                # Append the current index to the left end of the deque
                deq.appendleft(i)

        return res