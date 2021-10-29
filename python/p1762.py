class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        top = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > top:
                ans.append(i)
                top = heights[i]
        return ans[::-1]
