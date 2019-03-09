/*
Fibonacci
*/
func climbStairs(n int) int {
    stats := [3]int{1, 2, 3}
    if n <= 3 {
        return stats[n-1]
    }
    for i := 4; i <= n; i++ {
        temp := stats[1] + stats[2]
        stats[0] = stats[1]
        stats[1] = stats[2]
        stats[2] = temp
    }
    return stats[2]
}
