from collections import defaultdict
from collections import deque


class Solution:
    def alienOrder(self, words):
        indeg = defaultdict(int)
        edges = defaultdict(list)

        charset = set()
        for word in words:
            for c in word:
                charset.add(c)

        for i in range(len(words) - 1):
            l1 = len(words[i])
            l2 = len(words[i + 1])
            diff = False

            for j in range(min(l1, l2)):
                if words[i][j] != words[i + 1][j]:
                    indeg[words[i + 1][j]] += 1
                    edges[words[i][j]].append(words[i + 1][j])
                    diff = True
                    break

            if l1 > l2 and not diff:
                return ""

        q = deque()

        for k in charset:
            if indeg[k] == 0:
                q.append(k)

        cnt = 0
        ans = []
        while q:
            cnt += 1
            t = q.popleft()
            ans.append(t)
            for k in edges[t]:
                indeg[k] -= 1
                if indeg[k] == 0:
                    q.append(k)

        if cnt != len(charset):
            return ""
        return "".join(ans)


s = Solution()
print(s.alienOrder(["abc", "ab"]))
