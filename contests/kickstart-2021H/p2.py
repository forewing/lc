lookup = {
    'U': set(),
    'R': {0},
    'Y': {1},
    'B': {2},
    'O': {0, 1},
    'P': {0, 2},
    'G': {1, 2},
    'A': {0, 1, 2},
}

total = {0, 1, 2}


def solve(n, s):
    pens = [False] * 3
    ans = 0
    for c in s:
        for p in total - lookup[c]:
            pens[p] = False
        for p in lookup[c]:
            if not pens[p]:
                ans += 1
                pens[p] = True
    return ans


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        s = input()
        print(f"Case #{i+1}: {solve(n, s)}")
