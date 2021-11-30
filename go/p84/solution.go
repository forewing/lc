package main

const (
	problemSize = 100000
)

var (
	stack = make([]int, problemSize)
	left  = make([]int, problemSize)
	right = make([]int, problemSize)
)

func largestRectangleArea(heights []int) int {
	n := len(heights)

	si := 0
	for i := 0; i < n; i++ {
		if si == 0 {
			left[i] = 0
			stack[si] = i
			si++
		} else {
			for si != 0 && heights[stack[si-1]] >= heights[i] {
				si--
			}
			if si == 0 {
				left[i] = 0
			} else {
				left[i] = stack[si-1] + 1
			}
			stack[si] = i
			si++
		}
	}

	si = 0
	for i := n - 1; i >= 0; i-- {
		if si == 0 {
			right[i] = n - 1
			stack[si] = i
			si++
		} else {
			for si != 0 && heights[stack[si-1]] >= heights[i] {
				si--
			}
			if si == 0 {
				right[i] = n - 1
			} else {
				right[i] = stack[si-1] - 1
			}
			stack[si] = i
			si++
		}
	}

	ans := 0
	for i := 0; i < n; i++ {
		t := (right[i] - left[i] + 1) * heights[i]
		if t > ans {
			ans = t
		}
	}

	return ans
}

func main() {
	largestRectangleArea(nil)
}
