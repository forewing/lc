class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        cnt_0 = 0
        pos_0 = -1
        l = len(nums)

        for i in range(l):
            if nums[i] == 0:
                cnt_0 += 1
                pos_0 = i
            else:
                prod *= nums[i]

        if cnt_0 >= 2:
            return [0] * l

        if cnt_0 == 1:
            return [0] * pos_0 + [prod] + [0] * (l - pos_0 - 1)

        ans = []
        for num in nums:
            ans.append(prod // num)
        return ans
