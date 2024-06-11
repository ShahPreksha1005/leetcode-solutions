class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Lengths of the two arrays
        m, n = len(nums1), len(nums2)
        total_length = m + n

        # Binary search boundaries
        low, high = 0, m

        while low <= high:
            # Partition nums1 at the middle
            partition_nums1 = (low + high) // 2
            # Partition nums2 at the ideal position
            partition_nums2 = (total_length + 1) // 2 - partition_nums1

            # Define boundary elements of partitions
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]

            # Check if the partition is valid
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                # Check if the total length is odd or even
                if total_length % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                high = partition_nums1 - 1
            else:
                low = partition_nums1 + 1
