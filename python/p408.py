class Solution:
    def is123(self, c):
        return c >= '0' and c <= '9'

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = len(word)
        if len(abbr) > l:
            return False

        ext = []
        num = 0
        for c in abbr:
            if self.is123(c):
                x = ord(c) - ord('0')
                if num == 0 and x == 0:
                    return False
                num *= 10
                num += x
                if num > l:
                    return False
            else:
                if num != 0:
                    for _ in range(num):
                        ext.append('*')
                    num = 0
                ext.append(c)

        if num != 0:
            for _ in range(num):
                ext.append('*')

        if l != len(ext):
            return False

        for i in range(l):
            if word[i] != ext[i] and ext[i] != '*':
                return False

        return True
