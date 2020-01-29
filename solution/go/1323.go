/*
@difficulty: easy
@tags: misc
@notes: Replace the first 6 to 9, can use #strings.replace.
*/
func maximum69Number (num int) int {
    str := strconv.Itoa(num)
    for i := 0; i < len(str); i++ {
        if str[i] == '6' {
            str = str[:i] + "9" + str[i+1:]
            res, _ := strconv.Atoi(str)
            return res
        }
    }
    return num
}
