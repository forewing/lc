class Solution:
    def __init__(self):
        self.hundred = "Hundred"
        self.split = ["INVALID", "Thousand", "Million", "Billion"]
        self.tens = ["INVALID", "INVALID", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                      "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    def get_100_999(self, num):
        hundred = num // 100
        remain = self.get_10_99(num % 100)
        if hundred > 0:
            return [self.ones[hundred], self.hundred] + remain
        return remain

    def get_10_99(self, num):
        if num < 10:
            return self.get_0_9(num)
        elif num < 20:
            return [self.teens[num % 10]]
        else:
            return [self.tens[num // 10]] + self.get_0_9(num % 10)

    def get_0_9(self, num):
        if num == 0:
            return []
        return [self.ones[num]]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.ones[0]

        result = []
        for split in range(0, 4):
            remain = num % 1000
            num //= 1000
            if remain:
                result = self.get_100_999(remain) + ([self.split[split]] if split > 0 else []) + result
        return " ".join(result)
