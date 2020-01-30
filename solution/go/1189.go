/*
@difficulty: easy
@tags: misc
@notes: Hashmap.
*/
func maxNumberOfBalloons(text string) int {
    stats := make(map[rune]int)
    for _, val := range text {
        stats[val] += 1
    }
    res := 10000
    balon := map[rune]int {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1,
    }
    for key, val := range balon {
        _, ok := stats[key]
        if ok {
            res = min(res, stats[key]/val)
        } else {
            return 0
        }
    }
    return res
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
