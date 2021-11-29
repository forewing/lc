package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestBSTSubtree(root *TreeNode) int {
	_, r, _, _ := _largestBSTSubtree(root)
	return r
}

func _largestBSTSubtree(root *TreeNode) (ok bool, result, min, max int) {
	if root == nil {
		return false, 0, 0, 0
	}

	if root.Left == nil && root.Right == nil {
		return true, 1, root.Val, root.Val
	}

	ok1, r1, min1, max1 := _largestBSTSubtree(root.Left)
	ok2, r2, min2, max2 := _largestBSTSubtree(root.Right)

	result = r1
	if r2 > result {
		result = r2
	}

	if (root.Left != nil && (!ok1 || root.Val <= max1)) || (root.Right != nil && (!ok2 || root.Val >= min2)) {
		return false, result, 0, 0
	}

	if root.Left == nil {
		return true, r2 + 1, root.Val, max2
	} else if root.Right == nil {
		return true, r1 + 1, min1, root.Val
	}

	return true, r1 + r2 + 1, min1, max2
}

func main() {
	largestBSTSubtree(nil)
}
