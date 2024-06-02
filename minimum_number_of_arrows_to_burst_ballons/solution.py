### Minimum Number of Arrows to Burst Balloons


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points array by x-start
        points.sort()
        n_arrow, arrow = 1, points[-1][0]
        
        # Iterate through the points array from right to left
        for i in range(len(points) - 2, -1, -1):
            if not points[i][0] <= arrow <= points[i][1]:
                arrow = points[i][0]
                n_arrow += 1
        return n_arrow