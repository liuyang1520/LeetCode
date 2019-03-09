/*
Use a map
*/
func containsDuplicate(nums []int) bool {
    set := make(map[int]int)
    for _, val := range nums {
        if _, ok := set[val]; ok {
            return true
        } else {
            set[val] = 1
        }
    }
    return false
}
