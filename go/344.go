/*
No builtin function available, has to do it manually.
*/
func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(s) - 1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
