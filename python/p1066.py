class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.workers = workers
        self.bikes = bikes
        self.nw = len(workers)
        self.nb = len(bikes)

        return self.search(0, 0)

    def search(self, worker, bike_used):
        if worker == self.nw:
            return 0

        ans = float('inf')

        for bike in range(self.nb):
            if bike_used & (1 << bike) == 0:
                ans = min(ans, self.search(worker + 1, bike_used | (1 << bike)) +
                          abs(self.workers[worker][0] - self.bikes[bike][0]) +
                          abs(self.workers[worker][1] - self.bikes[bike][1]))
        return ans
