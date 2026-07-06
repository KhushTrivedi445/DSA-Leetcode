class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers for nums1, nums2, and the end of nums1 array
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        # Merge elements from right to left
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        