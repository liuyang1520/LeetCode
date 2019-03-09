/*
This solution use map, with O(n) for both space and time complexity.
Boyer-Moore Voting Algorithm can make it O(1) for space and O(n) for time.
*/
func majorityElement(nums []int) int {
    counter := make(map[int]int)
    for _, val := range nums {
        if _, ok := counter[val]; ok {
            counter[val]++
        } else {
            counter[val] = 1
        }
        if float64(counter[val]) >= float64(len(nums))/2 {
            return val
        }
    }
    return -1
}
