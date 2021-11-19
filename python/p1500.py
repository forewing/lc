import heapq


class FileSharing:

    def __init__(self, m):
        self.uid_pool = []
        self.uid_tail = 1

        self.files = [set() for _ in range(m + 1)]
        self.userfiles = {}

    def join(self, ownedChunks):
        id = self.uid_tail
        if self.uid_pool:
            id = heapq.heappop(self.uid_pool)
        else:
            self.uid_tail += 1

        for chunk in ownedChunks:
            self.files[chunk].add(id)

        self.userfiles[id] = set(ownedChunks)
        print(self.files)

        return id

    def leave(self, userID):
        heapq.heappush(self.uid_pool, userID)
        for file in self.userfiles[userID]:
            self.files[file].remove(userID)
        del self.userfiles[userID]

    def request(self, userID, chunkID):
        ret = sorted(self.files[chunkID])
        if ret:
            self.userfiles[userID].add(chunkID)
            self.files[chunkID].add(userID)
        return ret

# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)
