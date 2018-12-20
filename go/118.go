/*
Build the triangle level by level
*/
func generate(numRows int) [][]int {
    if numRows == 0 { return [][]int{} }
    res := make([][]int, 0)
    res = append(res, []int{1})
    for i := 2; i <= numRows; i++ {
        temp := make([]int, 0)
        for j := 0; j <= i-1; j++ {
            if j == 0 || j == i-1 {
                temp = append(temp, 1)
            } else {
                temp = append(temp, res[i-2][j] + res[i-2][j-1])
            }
        }
        res = append(res, temp)
    }
    return res
}
