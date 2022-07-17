from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)

        upper = sum(weights)
        lower = max(weights)
        cup = 0

        while upper > lower:
            cap = (upper + lower) // 2
            if self.ok(weights, cap, days):
                upper = cap
            else:
                lower = cap+1

        return lower

    def ok(self, weights, max_cap, max_days):
        days = 1
        cap = 0

        for weight in weights:
            cap += weight
            if cap <= max_cap:
                continue
            days += 1
            cap = weight
            if days > max_days:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
    print(s.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
    print(s.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))
