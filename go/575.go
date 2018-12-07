/*
Count how many different num appears then choose min(unique_nums, len(candies)/2)
*/
func distributeCandies(candies []int) int {
    stats := make(map[int]bool)
    for _, num := range candies {
        if !stats[num] {
            stats[num] = true
        }
    }
    res := len(candies) / 2
    if len(stats) < res {
        return len(stats)
    } else {
        return res
    }
}
