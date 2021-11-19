class Solution:
    def encode(self, num: int) -> str:
        return format(num + 1, "b")[1:]
