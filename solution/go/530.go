/*
Didn't read the question carefully. The tree is BST actually, so no need to sort if push all elements to left of the array.
*/
func getMinimumDifference(root *TreeNode) int {
    nums := make([]int, 0)
    helper(root, &nums)
    sort.Ints(nums)
    minDiff := math.MaxInt32
    for i := 0; i < len(nums) - 1; i++ {
        diff := nums[i+1] - nums[i]
        if diff < minDiff {
            minDiff = diff
        }
    }
    return minDiff
}

func helper(root *TreeNode, nums *[]int) {
    if root == nil {
        return
    }
    *nums = append(*nums, root.Val)
    if root.Left != nil {
        helper(root.Left, nums)
    }
    if root.Right != nil {
        helper(root.Right, nums)
    }
    return
}
