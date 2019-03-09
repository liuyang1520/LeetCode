/*
The math solution: https://en.wikipedia.org/wiki/Digital_root
This is the for loop solution.
*/
func addDigits(num int) int {
    str := strconv.Itoa(num)
    for len(str) > 1 {
        value := 0
        for _, val := range str {
            if i, err := strconv.Atoi(string(val)); err == nil {
                value += i
            }
        }
        str = strconv.Itoa(value)
    }
    if i, err := strconv.Atoi(str); err == nil {
        return i
    }
    return 0
}
