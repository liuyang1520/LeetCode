/*
One iteration, change to string
*/
func binaryGap(N int) int {
    n := int64(N)
    binary := strconv.FormatInt(n, 2)
    maxDis, lastIndex := 0, -1
    for i := 0; i < len(binary); i++ {
        if binary[i] == '1' {
            if lastIndex >= 0 && maxDis < i - lastIndex {
                maxDis = i - lastIndex
            }
            lastIndex = i
        }
    }
    return maxDis
}
