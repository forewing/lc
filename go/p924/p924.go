package p924

import "sort"

/*
 * @lc app=leetcode id=924 lang=golang
 */

// @lc code=start

var (
	parent []int
)

func find(index int) int {
	for parent[index] != index {
		parent[index] = parent[parent[index]]
		index = parent[index]
	}
	return index
}

func union(a, b int) {
	ap := find(a)
	bp := find(b)
	if ap != bp {
		parent[ap] = bp
	}
}

func minMalwareSpread(graph [][]int, initial []int) int {
	n := len(graph)
	parent = parent[:0]
	for i := 0; i < n; i++ {
		parent = append(parent, i)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if graph[i][j] == 1 {
				union(i, j)
			}
		}
	}

	size := make([]int, n)
	for i := 0; i < n; i++ {
		size[find(i)]++
	}

	infected := make([]int, n)
	for _, t := range initial {
		infected[find(t)]++
	}

	sort.Slice(initial, func(i int, j int) bool {
		return initial[i] > initial[j]
	})

	ans := n
	best := 0
	for _, t := range initial {
		if infected[find(t)] == 1 {
			if best2 := size[find(t)]; best2 >= best {
				best = best2
				ans = t
			}
		} else if best == 0 {
			ans = t
		}
	}

	return ans
}

// @lc code=end
