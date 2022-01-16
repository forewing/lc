package main

import "sort"

type Record struct {
	val     int
	isStart bool
}
type Records []Record

func (r Records) Len() int {
	return len(r)
}

func (r Records) Less(i, j int) bool {
	if r[i].val < r[j].val || (r[i].val == r[j].val && !r[i].isStart && r[j].isStart) {
		return true
	}
	return false
}

func (r Records) Swap(i, j int) {
	r[i], r[j] = r[j], r[i]
}

func minMeetingRooms(intervals [][]int) int {
	records := make(Records, len(intervals)*2)
	for i := range intervals {
		records[i*2] = Record{
			val:     intervals[i][0],
			isStart: true,
		}
		records[i*2+1] = Record{
			val:     intervals[i][1],
			isStart: false,
		}
	}
	sort.Sort(records)

	ans := 0
	cur := 0
	for i := range records {
		if records[i].isStart {
			cur++
			if cur > ans {
				ans = cur
			}
		} else {
			cur--
		}
	}

	return ans
}

func main() {}
