/*
Two pointers
*/
func removeElement(nums []int, val int) int {
    first, last := 0, len(nums) - 1
    for ; first <= last; first++ {
        for ; last >= 0 && nums[last] == val; last-- {}
        if first > last {
            break
        }
        if nums[first] == val {
            nums[first], nums[last] = nums[last], nums[first]
        }
    }
    return last + 1
}
