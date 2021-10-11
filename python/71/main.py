class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        paths = path.split("/")
        for p in paths:
            if not p or p == ".":
                continue
            if p != "..":
                result.append(p)
            elif result:
                result.pop()

        return "/" + "/".join(result)
