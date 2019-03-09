/*
Store the visited values to avoid cycles.
*/
func isHappy(n int) bool {
    history := make(map[int]bool)
    for true {
        if history[n] { return false }
        subtotal, temp := 0, n
        for temp != 0 {
            subtotal += (temp % 10) * (temp % 10)
            temp = temp / 10
        }
        if subtotal == 1 {
            return true
        } else {
            history[n] = true
            n = subtotal
        }
    }
    return false
}
