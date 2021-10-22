package p437

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) int {
	if root == nil {
		return 0
	}
	return search(root, targetSum) + pathSum(root.Left, targetSum) + pathSum(root.Right, targetSum)
}

func search(node *TreeNode, target int) int {
	if node == nil {
		return 0
	}

	result := 0
	if node.Val == target {
		result = 1
	}
	result += search(node.Left, target-node.Val) + search(node.Right, target-node.Val)
	return result
}
