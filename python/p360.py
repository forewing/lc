class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        return sorted(map(lambda x: a * x * x + b * x + c, nums))