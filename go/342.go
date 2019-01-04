/*
- Use logarithm, 4^x = num, x = log(num) / log(4)
- num & 0x55555555, 0b10101010... makes sure it is not power of 2
- 4^n - 1^n = (4-1)*(...) = 3*x
*/
func isPowerOfFour(num int) bool {
    if num <= 0 {
        return false
    }
    temp := math.Log(float64(num)) / math.Log(4)
    return temp == math.Trunc(temp)
}

func isPowerOfFour(num int) bool {
    return num > 0 && (num & (num-1)) == 0 && (num & 0x55555555) == num
}

func isPowerOfFour(num int) bool {
    return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0
}
