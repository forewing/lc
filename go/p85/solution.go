package main

const (
	problemSize = 200
)

var (
	stack = make([]int, problemSize)
	left  = make([]int, problemSize)
	right = make([]int, problemSize)
)

func maximalRectangle(matrix [][]byte) int {
	n := len(matrix)

	if n == 0 {
		return 0
	}

	m := len(matrix[0])

	for i := 0; i < n; i++ {
		matrix[i][0] -= '0'
		for j := 1; j < m; j++ {
			matrix[i][j] -= '0'
			if matrix[i][j] == 1 {
				matrix[i][j] = matrix[i][j-1] + 1
			}
		}
	}

	ans := 0

	for j := 0; j < m; j++ {
		si := 0
		for i := 0; i < n; i++ {
			if si == 0 {
				left[i] = 0
				stack[si] = i
				si++
			} else {
				for si != 0 && matrix[stack[si-1]][j] >= matrix[i][j] {
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
				for si != 0 && matrix[stack[si-1]][j] >= matrix[i][j] {
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

		for i := 0; i < n; i++ {
			t := (right[i] - left[i] + 1) * int(matrix[i][j])
			if t > ans {
				ans = t
			}
		}
	}

	return ans
}

func main() {
	// maximalRectangle([][]byte{{'1', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'}})
	maximalRectangle([][]byte{{'1', '1'}})
}
