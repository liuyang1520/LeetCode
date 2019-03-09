// Use hashmap to speed up the searching process
func numJewelsInStones(J string, S string) int {
    jewels := make(map[rune]bool)
    for _, val := range J {
        if _, ok := jewels[val]; !ok {
            jewels[val] = true
        }
    }
    count := 0
    for _, val := range S {
        if _, ok := jewels[val]; ok {
            count++
        }
    }
    return count
}
