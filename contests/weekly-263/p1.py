class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(" ")
        l = []
        for word in words:
            o = ord(word[0])
            if o >= ord('0') and o <= ord('9'):
                l.append(int(word))
        for i in range(len(l) - 1):
            if l[i] >= l[i + 1]:
                return False
        return True
