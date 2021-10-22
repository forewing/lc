package p993

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type matchResult int

const (
	matchNo matchResult = 0
	matchX  matchResult = 1
	matchY  matchResult = 2
)

var (
	gx, gy int
	px, py int
	dx, dy int
)

func isCousins(root *TreeNode, x int, y int) bool {
	gx = x
	gy = y
	px = 0
	py = 0
	dx = 0
	dy = 0

	start := &TreeNode{
		Val:  0,
		Left: root,
	}
	search(start, 0)
	return dx == dy && px != py
}

func search(node *TreeNode, d int) matchResult {
	fmt.Println(dx, dy, px, py)
	if node == nil {
		return matchNo
	}

	ret := matchNo
	if node.Val == gx {
		ret = matchX
		dx = d
	} else if node.Val == gy {
		ret = matchY
		dy = d
	}

	rl := search(node.Left, d+1)
	rr := search(node.Right, d+1)

	if rl == matchX || rr == matchX {
		px = node.Val
	}
	if rl == matchY || rr == matchY {
		py = node.Val
	}

	return ret
}
