
## Daily Temperatures

### Problem Description:

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i]` equal to `0` instead.

### Example:

Refer to the provided examples.

### Constraints:

- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

### Approach:

To solve this problem efficiently, we can use a monotonic stack approach. We iterate through the temperatures array from right to left and maintain a deque to store indices of temperatures. We compare each temperature with the temperature at the left end of the deque and calculate the number of days to wait for a warmer temperature.

### Code Implementation:

Refer to the provided code.

---
