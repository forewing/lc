from typing import List
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        heights = []
        ans = 0
        for (_, h) in envelopes:
            ind = bisect.bisect_left(heights, h)
            if ind == len(heights):
                heights.append(h)
            else:
                heights[ind] = h
            ans = max(ans, ind + 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
    print(s.maxEnvelopes([[1, 1], [1, 1], [1, 1]]))
