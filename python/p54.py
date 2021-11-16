class Solution:

    def spiralOrder(self, matrix):
        mx = [0, 1, 0, -1]
        my = [1, 0, -1, 0]

        n = len(matrix)
        m = len(matrix[0])
        nx, ny = 0, 0
        # 0> 1V 2< 3^
        direct = 0
        limit = [m, n, -1, 0]

        test = {
            0: lambda x, y: y < limit[0],
            1: lambda x, y: x < limit[1],
            2: lambda x, y: y > limit[2],
            3: lambda x, y: x > limit[3],
        }

        def update(d):
            if d <= 1:
                limit[d] -= 1
            else:
                limit[d] += 1

        ans = []
        while True:
            # print(direct, nx, ny, limit)
            ans.append(matrix[nx][ny])
            tx, ty = nx + mx[direct], ny + my[direct]
            if not test[direct](tx, ty):
                update(direct)
                direct = (direct + 1) % 4
                nx += mx[direct]
                ny += my[direct]
                if not test[direct](nx, ny):
                    break
            else:
                nx, ny = tx, ty

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(s.spiralOrder([[1, 2], [3, 4]]))
    print(s.spiralOrder([[1], [2]]))
    print(s.spiralOrder([[1]]))
