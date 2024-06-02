## Minimum Number of Arrows to Burst Balloons

### Problem Description:

There are some spherical balloons taped onto a flat wall represented by the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose horizontal diameter stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is burst by an arrow shot at `x` if `xstart <= x <= xend`. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return the minimum number of arrows that must be shot to burst all balloons.

### Example:

Refer to the provided examples.

### Constraints:

- 1 <= points.length <= 10^5
- points[i].length == 2
- -2^31 <= xstart < xend <= 2^31 - 1

### Approach:

We can solve this problem by sorting the balloons by their x-start coordinates and then iterating through them. For each balloon, we check if its x-start coordinate is within the range of the previous balloon's x-end coordinate. If not, we need to shoot another arrow. We repeat this process until we have processed all the balloons.

### Code Implementation:

Refer to the provided code.
