def solve(s, f):
    dist = [100] * 26
    avaliable = set(map(lambda c: ord(c) - ord('a'), f))
    for i in range(26):
        if i in avaliable:
            dist[i] = 0
        else:
            for a in avaliable:
                dist[i] = min(dist[i], abs(a-i), 26-abs(a-i))
    ans = 0
    for c in s:
        ans += dist[ord(c) - ord('a')]
    return ans


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        s = input()
        f = input()
        print(f"Case #{i+1}: {solve(s, f)}")
