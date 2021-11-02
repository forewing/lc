class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = len(nums1)
        result = [0] * total
        i1, i2 = 0, 0
        ir = 0
        while True:
            while (i1 >= m and i2 < n) or (i2 < n and nums2[i2] <= nums1[i1]):
                result[ir] = nums2[i2]
                i2 += 1
                ir += 1
            while (i2 >= n and i1 < m) or (i1 < m and nums1[i1] <= nums2[i2]):
                result[ir] = nums1[i1]
                i1 += 1
                ir += 1
            if i1 == m and i2 == n:
                break
        for i in range(total):
            nums1[i] = result[i]
        return
