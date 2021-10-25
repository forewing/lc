class Solution:
    def __init__(self):
        self.transform = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM", "", "", "", "", "", ""],
        ]

    def intToRoman(self, num: int) -> str:
        result = [""] * 4
        for i in range(4):
            if num <= 0:
                break
            result[3 - i] = self.transform[i][num % 10]
            num //= 10
        return "".join(result)
