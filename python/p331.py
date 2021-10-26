class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        cnt = 1
        for i, x in enumerate(nodes):
            if x == "#":
                cnt -= 1
                if cnt == 0:
                    return i == len(nodes) - 1
            else:
                cnt += 1
        return False
