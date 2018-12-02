/*
If 0, reset cur, O(n) time
*/
func findMaxConsecutiveOnes(nums []int) int {
    max, cur := 0, 0
    for _, val := range nums {
        if val == 0 {
            cur = 0
        } else {
            cur += 1
            if cur > max {
                max = cur
            }
        }
    }
    return max
}
