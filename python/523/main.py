class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        table = set()
        table.add(0)

        n = len(nums)
        sum = nums[0] % k
        lastsum = sum

        for i in range(1, n):
            t = nums[i]

            sum += t
            sum %= k
            if sum in table:
                return True

            table.add(lastsum)
            lastsum = sum

        return False
