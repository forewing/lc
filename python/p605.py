class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        tot = len(flowerbed)

        l = 0
        while l < tot and flowerbed[l] == 0:
            l += 1
        if l == tot:
            return (tot + 1) // 2 >= n
        ans += l // 2

        r = tot - 1
        while r >= 0 and flowerbed[r] == 0:
            r -= 1
        ans += (tot - 1 - r) // 2

        last = l
        for i in range(l + 1, r + 1):
            if flowerbed[i] == 1:
                ans += max(0, (i - last - 2) // 2)
                last = i

        return ans >= n
