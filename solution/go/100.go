/*
Recursively check val, left and right values in the treeNode
*/
func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p == nil && q == nil {
        return true
    } else if (p != nil && q == nil) || (q != nil && p == nil) {
        return false
    } else if p.Val != q.Val {
        return false
    } else {
        return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
    }
}
