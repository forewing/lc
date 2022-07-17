from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                if k == 0:
                    dic[num].add(num)
                continue

            dic[num] = set()
            if k == 0:
                continue
            if num+k in dic:
                dic[num+k].add(num)
            if num-k in dic:
                dic[num-k].add(num)

        ans = 0
        for k in dic:
            ans += len(dic[k])

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findPairs(nums=[3, 1, 4, 1, 5], k=2))
    print(s.findPairs(nums=[1, 2, 3, 4, 5], k=1))
    print(s.findPairs(nums=[1, 3, 1, 5, 4], k=0))
