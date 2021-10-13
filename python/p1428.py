# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        c = cols - 1
        while c >= 0:
            if binaryMatrix.get(0, c) == 0:
                break
            c -= 1

        r = 1
        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 0:
                r += 1
            else:
                c -= 1

        if c == cols - 1:
            return -1
        return c + 1


# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         rows, cols = binaryMatrix.dimensions()
#         ans = cols + 1
#         for r in range(rows):
#             cl = 0
#             cr = cols - 1
#             anst = cols + 1
#             while cl <= cr:
#                 cm = (cl + cr) // 2
#                 if binaryMatrix.get(r, cm) == 0:
#                     cl = cm + 1
#                 else:
#                     anst = cm
#                     cr = cm - 1
#             ans = min(ans, anst)

#         if ans == cols + 1:
#             return -1
#         return ans
