/*
Use hashmap to store the frequency of each char
*/
func isAnagram(s string, t string) bool {
    stats := make(map[rune]int)
    if len(s) > len(t) {
        t, s = s, t
    }
    for _, value := range s {
        stats[value] += 1
    }
    for _, value := range t {
        if val, ok := stats[value]; ok && val > 0 {
            stats[value] -= 1
        } else {
            return false
        }
    }
    return true
}
