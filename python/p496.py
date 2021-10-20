class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = dict()
        for num in nums1:
            result[num] = -1
        s = []
        for num in nums2:
            while s and num > s[-1]:
                result[s[-1]] = num
                s.pop()
            if num in result:
                s.append(num)
        return [result[num] for num in nums1]
