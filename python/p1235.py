from typing import List
import bisect


class Solution:
    def __init__(self):
        self.jobs = None
        self.result = None
        self.total = 0

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.total = len(startTime)
        self.result = [-1] * self.total
        self.jobs = list(zip(startTime, endTime, profit))
        self.jobs.sort(key=lambda job: job[0])
        return self.search(0)

    def search(self, index):
        if index >= self.total:
            return 0

        if self.result[index] != -1:
            return self.result[index]

        job = self.jobs[index]
        next_index = bisect.bisect_left(self.jobs, job[1], lo=index + 1, key=lambda job: job[0])

        self.result[index] = max(self.search(index + 1), job[2] + self.search(next_index))
        return self.result[index]


if __name__ == "__main__":
    s = Solution()

    print(s.jobScheduling(
        startTime=[1, 2, 3, 3],
        endTime=[3, 4, 5, 6],
        profit=[50, 10, 40, 70]))

    print(s.jobScheduling(
        startTime=[1, 2, 3, 4, 6],
        endTime=[3, 5, 10, 6, 9],
        profit=[20, 20, 100, 70, 60]))

    print(s.jobScheduling(
        startTime=[1, 1, 1],
        endTime=[2, 3, 4],
        profit=[5, 6, 4]))
