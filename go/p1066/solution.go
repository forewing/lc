package p1066

var (
	dist [][]int
	wn   int
	bn   int
)

func abs(x int) int {
	if x >= 0 {
		return x
	}
	return -x
}

func assignBikes(workers [][]int, bikes [][]int) int {
	wn = len(workers)
	bn = len(bikes)
	dist = make([][]int, wn)
	for i := 0; i < wn; i++ {
		dist[i] = make([]int, bn)
		for j := 0; j < bn; j++ {
			dist[i][j] = abs(workers[i][0]-bikes[j][0]) + abs(workers[i][1]-bikes[j][1])
		}
	}

	return search(0, 0)
}

func search(worker, bike_used int) int {
	if worker == wn {
		return 0
	}
	ans := 10000000
	for bike := 0; bike < bn; bike++ {
		if bike_used&(1<<bike) == 0 {
			tmp := search(worker+1, bike_used|(1<<bike)) + dist[worker][bike]
			if tmp < ans {
				ans = tmp
			}
		}
	}
	return ans
}
