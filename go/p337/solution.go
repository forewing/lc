package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(root *TreeNode) int {
	return max(_rob(root))
}

func _rob(root *TreeNode) (int, int) {
	if root == nil {
		return 0, 0
	}

	l0, l1 := _rob(root.Left)
	r0, r1 := _rob(root.Right)

	return max(l0, l1) + max(r0, r1), l0 + r0 + root.Val
}

func main() {
	rob(nil)
}
